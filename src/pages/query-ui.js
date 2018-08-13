import * as React from 'react';
import jq from 'jquery';
import axios from 'axios';
import TextQueryUI from './text-query-ui';
import RangeQueryUI from './range-query-ui';
import SelectMultipleQueryUI from './select-multiple-query-ui';
import SelectOneQueryUI from './select-one-query-ui';
import ProximityQueryUI from './proximity-query-ui';

export default class QueryUI extends React.PureComponent {

	constructor(props) {
		super(props);
		this.state = { 
			datafields: []
		};
	}

	componentDidMount = () => {
		document.querySelector('#query-reset').onclick = this._queryReset;
		document.querySelector('#query-submit').onclick = this._querySubmit;
		axios.get('datafields')
		.then(response => {
			this.setState({ datafields: response.data.datafields });
		});
	}

	componentDidUpdate() {
		if (this.state.datafields.length > 0) {
			document.querySelectorAll('#query-area input[type=checkbox].query-group')
					.forEach(element => element.onclick = this._checkBox);
		}
	}

	_checkBox() {
    var checked = $(this).prop('checked');
    if (checked) { // CHECK
      // ENABLE OPERAND UI
      $(this).parent('label').parent('div').find('.operand-ui').prop('disabled', false);
      $(this).parent('label').parent('div').find('input.output-only').prop('disabled', true);
      $(this).parent('label').parent('div').find('.operand-ui').removeClass('disabled');
      $($(this).parent('label').parent('div').find('.operand-ui.modal')[0]).modal('show');
    }
    else { // UNCHECK
      // DISABLE QUERY VALUE OPTIONS
      $(this).parent('label').parent('div').find('.operand-ui').prop('disabled', true);
      $(this).parent('label').parent('div').find('.operand-ui').addClass('disabled');
    }
	}

	_querySubmit = () => {
		// COLLECT DATASOURCES, FIELD NAMES, AND OPERANDS FOR NON-EMPTY OPERAND UIS
    var query_elems = [];
    var tables_needed = [];

    var query_checkboxes = jq('.query-group');
    for (var i = 0; i < query_checkboxes.length; i++) {
      var query_checkbox = jq(query_checkboxes[i]);

      if (query_checkbox.prop('checked')) { // ONLY FOR SELECTED QUERY UIS
        var type = query_checkbox.data('query-type');
        var table = query_checkbox.data('table')/*.split(',')*/;
        var field = query_checkbox.data('field');
        var clause = '';

        // Get input value per type and generate query clause
        // NOTE: Carto uses single quote for sql but not double quote!
        switch (type) {

          case 'text':
            var input = jq('#' + field + '-input');
            var val = input.val().trim();
            clause = ' ' + field + ' LIKE \'' + val + '\'';
            break;

          case 'range':
            var input_min = jq('#' + field + '-min-input');
            var input_max = jq('#' + field + '-max-input');
            var val_min = parseInt(input_min.val().trim());
            var val_max = parseFloat(input_max.val().trim());
            if (val_min && !isNaN(val_min)) {
              clause += ' ' + field + ' >= ' + val_min;
            }
            if (val_max && !isNaN(val_max)) {
              if (clause != '') clause += ' and';
              clause += ' ' + field + ' <= ' + val_max;
            }
            break;

          case 'select_one':
            var input = jq('#' + field + '-input');
            var val = input.val().trim();
            clause = ' ' + field + ' = \'' + val + '\'';
            break;

          case 'select_multiple':
            var input = jq('#' + field + '-input');
            var vals = input.val().split(',');
            for(var valIndex in vals) {
              vals[valIndex] = '\'' + vals[valIndex] + '\'';
            }
            clause = field + ' = ' + vals.join(' or ' + field + ' = ');
            break;

          case 'proximity':
            var distance_input_miles = parseFloat(jq('#' + field + '-distance-input').val().replace(',', ''));
            var location_input = jq('#' + field + '-location-input').val().trim();
            var location_input_escaped = encodeURI(location_input.replace(/[^0-9a-z\s\-_,\.]/gi, ''));
            if (!isNaN(distance_input_miles) && distance_input_miles > 0 && location_input_escaped) {
              var distance_meters = distance_input_miles * 1609.34;

              var http = new XMLHttpRequest();
              var geocode_request_url = "geocode/" + location_input_escaped
              http.open("GET", geocode_request_url, false);
              http.send();
              var response_json = JSON.parse(http.responseText)
              if (!response_json.total_rows || response_json.total_rows == 0) {
                console.error('Geocoding could not find a location for the query: ', location_input)
                return;
              }
              var location_geocoded = response_json.rows[0].cdb_geocode_street_point;

              clause = 'ST_DWithin(' + field + '::geography, ST_GeomFromWKB(decode(\'' + location_geocoded + '\', \'hex\')), ' + distance_meters + ')';
            }
            break;
          default:
            console.error(type, ': unexpected query type');
            return;
        }
        jq.merge(tables_needed, table);
        jq.unique(tables_needed);
        var query_elem = {
          type: type,
          table: table,
          field: field,
          clause: clause
        };
        query_elems.push(query_elem);
      }
    }

    // This information should be included in the query string below.
    // console.log('query_elems', query_elems);
    // console.log('tables_needed', tables_needed);

    // Nothing to query; TODO: an error message?
    if (tables_needed.length == 0 || query_elems.length == 0) return;

    // Build query string per table
    var query_per_table = {};
    for (var i = 0; i < tables_needed.length; i++) {
      var table = tables_needed[i];
      query_per_table[table] = 'SELECT * FROM ' + table + ' WHERE';
    }

    let filter_clauses = {};

    query_elems.forEach(query_elem => query_elem.table.forEach(table => {
    	filter_clauses[table] = '';
    }));

    for (var i = 0; i < query_elems.length; i++) {
      var query_elem = query_elems[i];
      var tables = query_elem.table;

      for (var j = 0; j < tables.length; j++) {
        var table = tables[j];
        filter_clauses[table] += ' (' + query_elem.clause + ' )';
        filter_clauses[table] += ' and';
      }
    }

    // Removing the following ' and'
    for (var i = 0; i < tables_needed.length; i++) {
      var table = tables_needed[i];
      var len = filter_clauses[table].length;
      filter_clauses[table] = filter_clauses[table].slice(0, len - ' and'.length);
      query_per_table[table] = query_per_table[table] + filter_clauses[table];
    }

    this.props.updateParcelWhereClause(filter_clauses.central_coast_joined);

    // Check the query_per_table; it should contain all the information on query you want to perform
    console.log('query_per_table', query_per_table);
    console.log('filter_clauses', filter_clauses);

    //
    // Apply query per case of combination
    //
    var layerqueries = {};

    var parcel_layer = this.props.layers['data']['Ag Parcels'];
    var point_layer = this.props.layers['data']['data_point'];
    var polygon_layer = this.props.layers['data']['data_polygon'];

    var parcel_table = this.props.tables['Ag Parcels'];
    var point_table = this.props.tables['data_point'];
    var polygon_table = this.props.tables['data_polygon'];

    var parcel_query = null;
    var point_query = null;
    var polygon_query = null;

    if (Object.keys(query_per_table).length == 1) {
      if (this.props.tables['Ag Parcels'] in query_per_table) {
        // Parcel-only query case
        parcel_query = query_per_table[this.props.tables['Ag Parcels']];
        point_query = 'SELECT ' + point_table + '.* FROM ' + point_table + ' INNER JOIN (' + parcel_query + ') as parcel ON ST_Intersects(' + point_table + '.the_geom, parcel.the_geom)';
        polygon_query = 'SELECT ' + polygon_table + '.* FROM ' + polygon_table + ' INNER JOIN (' + parcel_query + ') as parcel ON ST_Intersects(' + polygon_table + '.the_geom, parcel.the_geom)';
      }
      else if (this.props.tables['data_point'] in query_per_table) {
        // Point-only query case: not expected
        console.error('selected only data_point table');
      }
      else if (this.props.tables['data_polygon'] in query_per_table) {
        // Polygon-only query case: not expected
        console.error('selected only data_polygon table');
      }
    }
    else if (Object.keys(query_per_table).length == 2) {
      if ((this.props.tables['data_point'] in query_per_table) && (this.props.tables['data_polygon'] in query_per_table)) {
        // Survey-only query case
        parcel_query = 'SELECT ' + parcel_table + '.* FROM ' + parcel_table + ' INNER JOIN (' + point_query + ') as point ON ST_Intersects(' + parcel_table + '.the_geom, point.the_geom)\
          UNION\
          SELECT ' + parcel_table + '.* FROM ' + parcel_table + ' INNER JOIN (' + polygon_query + ') as polygon ON ST_Intersects(' + parcel_table + '.the_geom, polygon.the_geom)';
        point_query = query_per_table[this.props.tables['data_point']];
        polygon_query = query_per_table[this.props.tables['data_polygon']];
      }
      else {
        // Either point or polygon and parcel query case: not expected
        console.error('selected parcel and one survey table');
      }
    }
    else {
      // All the this.props.tables are involved
      parcel_query = query_per_table[this.props.tables['Ag Parcels']];
      point_query = query_per_table[this.props.tables['data_point']];
      polygon_query = query_per_table[this.props.tables['data_polygon']];
    }

    //
    // Apply queries for each layer
    //
    parcel_layer.setQuery(parcel_query);
    point_layer.setQuery(point_query);
    polygon_layer.setQuery(polygon_query);

    //
    // Send a query log item
    //
    layerqueries[parcel_table] = parcel_query;
    layerqueries[point_table] = point_query;
    layerqueries[polygon_table] = polygon_query;

    scrollToTop(500);
	}

	_queryReset = () => {	
		// Uncheck query UI checkboxes
    document.querySelectorAll('.query-group').forEach(query_ui => {
      if (query_ui.checked) {
        query_ui.click();
      }
    });

    let parcel_layer = this.props.layers['data']['Ag Parcels'];
    let point_layer = this.props.layers['data']['data_point'];
    let polygon_layer = this.props.layers['data']['data_polygon'];

    let parcel_table = this.props.tables['Ag Parcels'];
    let point_table = this.props.tables['data_point'];
    let polygon_table = this.props.tables['data_polygon'];

    parcel_layer.setQuery('SELECT * FROM ' + parcel_table);
    point_layer.setQuery('SELECT * FROM ' + point_table);
    polygon_layer.setQuery('SELECT * FROM ' + polygon_table);

    scrollToTop(500);
	}

	render() {
		let renderedDatafields = this.state.datafields.filter(datafield => datafield.use_for_query_ui)
		.map(datafield => {
				switch (datafield.type) {
					case 'text':
						return <TextQueryUI key={ datafield.name } {...datafield} />
						break; 
					case 'range':
						return <RangeQueryUI key={ datafield.name } {...datafield} />
						break; 
					case 'select_one':
						return <SelectOneQueryUI key={ datafield.name } {...datafield} />
						break;
					case 'select_multiple':
						return <SelectMultipleQueryUI key={ datafield.name } {...datafield} />
						break;
					case 'proximity':
						return <ProximityQueryUI key={ datafield.name } {...datafield} />
						break; 
					default:
						return;
				}
			});
		
		return (
			<div className='row'>
				<div className='col-xs-12'>
					<div className='well card'>
						<div className='row no-border-radius'>
					    <div id='query-area' className='form-group col-md-12'>
					      { renderedDatafields }
					    </div>
					  </div>
					  <div className='row'>
					    <div className='form-group col-md-offset-10 col-md-2'>
					      <button id='query-reset' className='btn btn-default query-buttons'>Reset</button>
					      <button id='query-submit' className='btn btn-primary query-buttons'>Submit</button>
					    </div>
					  </div>
			  	</div>
				</div>
		  </div>
		  );
  }

}