import * as React from 'react';
import ReactDOM from 'react-dom';
import MapComponent from './map-component';
import ParcelList from './parcel-list';
import QueryUI from './query-ui'
import { getMapConfig } from './carto-api-client';
import axios from 'axios';
import { makeSqlRequest } from './carto-sql-client';

export default class MapPage extends React.PureComponent {

	constructor(props) {
		super(props);
		this.state = {
	    cartoUserName: null,
	    tables: {},
	    layers: {},
	  };
	}

	componentDidMount = () => {
	  this._getAndStoreMapConfig(() => {
	  	
		  // console.info(`Configuration loaded: ${app.config}`);
		  // console.info(`Using configuration updated on ${app.config.pub_date}`);
		  // console.info(`Using Carto publication ${app.config.vizjson_url}`);
		  // app.config.optional_note && console.info('Note:', app.config.optional_note);

		  //
		  // Construct basemap layer
		  //
		  let mapObj = new L.Map('map', {
		    scrollWheelZoom: false, 
		    center: [36.65630120667228, -121.58981323242188],
		    zoom: 9
		  });

		  let basemap = L.tileLayer(
		    this.state.config.vizjson.layers[0].options.urlTemplate,
		    this.state.config.vizjson.layers[0].options
		  );

		  let layers = {'data': {}};
		  basemap.addTo(mapObj);
		  layers['basemap'] = basemap;

	    let cartoUserName = this.state.config.vizjson.layers[1].options.user_name;

	    this.setState({
	    	cartoUserName: cartoUserName,
	    	layers: layers,
	    	map: mapObj
	    }, () => {
			  for (let layerIndex in this.state.config.vizjson.layers[1].options.layer_definition.layers) {
			    this._setupTable(layerIndex);
			    this._setupLayer(layerIndex);
			  }
			});
	  });
	}

	_setupTable = (layerIndex) => {
		let layerDef = this.state.config.vizjson.layers[1].options.layer_definition.layers[layerIndex];
    let layerName = layerDef.options.layer_name;
    let tableName = layerDef.options.sql.toLowerCase().split('from')[1].trim();
    tableName = tableName.includes('.') ? tableName.split('.')[1] : tableName;
    let tables = this.state.tables;
    tables[layerName] = tableName;
    this.setState({ tables: tables });
	}

	_setupLayer = (layerIndex) => {
		let layerDef = this.state.config.vizjson.layers[1].options.layer_definition.layers[layerIndex];
		let layerName = layerDef.options.layer_name;
		cartodb.createLayer(this.state.map, {
	      user_name: this.state.cartoUserName,
	      type: layerDef.type,
	      sublayers: [layerDef.options]
	    }, 
	    { 
	      https: true
	    })
	    .addTo(this.state.map, layerDef.order)
	    .done(layer => {

	      let layers = this.state.layers;
	      layers['data'][layerName] = layer;
	      this.setState({ layers: layers });

	      if(layer.layers.length > 1) {
	        console.warn('Layer', layerName, 'has two or more sublayers:', layer);
	      }

	      layer.setInteraction(true);

				this._setupSearchBox(this.state.map);	
				this._setupLayerSelector(layerName, layerIndex);

	      layer.on('featureOver', function(e, latlon, pxPos, data, l) {
	        $('#map').css('cursor', 'pointer');

	        layer.on('featureOut', function(e, latlon, pxPos, data, l) {
	          $('#map').css('cursor', '-webkit-grab');
	        });
	      });

	      //
	      // Setup infowindow; click event handler
	      //
	      layer.on('featureClick', (e, latlng, pos, datapoint, _layer) => {
	        this._setupInfoWindow(latlng, datapoint, this.state.cartoUserName, tableName, layerDef);
	      });

	      //
	      // Setup legends; TODO: interactive legend to turn on/off
	      //
	      let legendDef = layerDef.legend;
	      if(legendDef.items != null && legendDef.visible) {
	        $('.cartodb-legend-stack').append(legendDef.template);
	      }

	      //
	      // Set the layer's visibility; according to the settings on Carto
	      //
	      layerDef.visible ? layer.show() : layer.hide();

	      console.info('A layer added:', layerName, layer);
	    })
	    .error(function(err) {
	      console.error('An error occured in creating layer:', err);
	    });
	}

	_setupLayerSelector = (layerName, layerIndex) => {
		let layerDef = this.state.config.vizjson.layers[1].options.layer_definition.layers[layerIndex];
    //
    // Setup a layer selector
    //
    if($('#map div.cartodb-layer-selector-box').length == 0) {
      // Setup an empty layer selector
      let layerSelectorTemplate = $('#layer-selector-template').html();
      $('#map').append(layerSelectorTemplate);
      // Toggle visibility of the layer selector dropdown menu
      $('a.layers.change-visibility').click(function(e) {
        if($('.cartodb-dropdown').css('display') == 'none') {
          $('.cartodb-dropdown').css('display', 'block');
        }
        else {
          $('.cartodb-dropdown').css('display', 'none');
        }
      });
    }

    // Fill out the layer selector
    let layerCnt = parseInt($('#map div.cartodb-layer-selector-box div.count').text());
    layerCnt++;
    $('#map div.cartodb-layer-selector-box div.count').text(layerCnt);

    // Setup an empty layer selector
    let toggleLayer = function(targetLayer) {
      this.state.layers.data[targetLayer].visible
      ? this.state.layers.data[targetLayer].hide()
      : this.state.layers.data[targetLayer].show();

      $.each($('a.switch.layer-switch'), function(i, o) {
        if(targetLayer == $(o).data('layer')) {
          if(this.state.layers.data[targetLayer].visible) {
            $(o).addClass('enabled');
          }
          else {
            $(o).removeClass('enabled');
          }
        }
      });
    };
    let layerSwitchTemplate = $($('#layer-switch-template').html());

    let layerSwitchLabel = $(layerSwitchTemplate.children('a.layer')[0]);
    layerSwitchLabel.data('layer', layerName);
    layerSwitchLabel.html(layerName);
    layerSwitchLabel.click(function(e) {
      toggleLayer($(this).data('layer'));
    });

    let layerSwitch = $(layerSwitchTemplate.children('a.switch')[0]);
    layerSwitch.data('layer', layerName);
    layerDef.visible ? layerSwitch.addClass('enabled') : layerSwitch.removeClass('enabled');

    layerSwitch.click(function(e) {
      toggleLayer($(this).data('layer'));
    });

    $('ul.layer-list').append(layerSwitchTemplate);
	}

	_setupInfoWindow = (latlng, datapoint, userName, tableName, layerDef) => {
	  if (layerDef === undefined) {
	    layerDef = this.state.config.vizjson.layers[1].options.layer_definition.layers
	        .filter(layer => layer.options.layer_name == "Ag Parcels")[0];
	    tableName = "central_coast_joined";
	    userName = "calo1";
	  }

	  // Remove existing markers, if any
	  $('div.dummy-div-icon').remove();

	  // Build a background query string
	  //
	  let clauses = [];
	  for(let key in datapoint) {
	    clauses.push(key + ' = ' + datapoint[key]);
	  }
	  let sql = 'SELECT * FROM ' + tableName + ' WHERE ' + clauses.join(' and ');
	  //console.log(sql);
	  //
	  // Send the background query for infowindow
	  //
	  makeSqlRequest(sql, userName)
	  .then(response => {
	    if(response.data.length > 1) {
	      console.warn('Background query results have two or more rows:', sql, response);
	      return;
	    }
	    else if (response.data.length == 0) {
	      console.warn('Background query does not return any rows:', sql);
	      return;
	    }
	    else {

	      //
	      // Prepare infowindow; find your data in res.rows[0]
	      //

	      // TODO: Later, I want to just call renderInfowindow(data);

	      //
	      // Parse Carto infowindow template
	      //
	      let parcelRow = response.data.rows[0];
	      let template = layerDef.infowindow.template.replace('\n', '').replace('\\"', '"').replace('\\\'', '\'');
	      let templateBody = template.match(/<div\s+class=("|')cartodb-popup-content("|')>[\S\s]*?<\/div>/gi)[0];
	      let templateLabels = templateBody.match(/<h[0-9]>[\S\s]*?<\/h[0-9]>/gi);
	      let templateCols = templateBody.match(/\{\{[\S\s]*?\}\}/gi);
	      let parseRes = '';
	      //console.log(templateLabels, templateCols);

	      if(templateLabels.length < templateCols.length) {
	        console.error(layerName, 'some columns don\'t have lables:');
	      }
	      else {
	        let popupForDataSource = $('.detail-popup .wrapper-per-source.data-from-' + tableName);
	        for(let labelIndex in templateLabels) {
	          // Labels to uppercase
	          let label = templateLabels[labelIndex].replace('_', ' ');
	          let tagH = label.match(/<.{2}>/i);
	          let tagT = label.match(/<\/.{2}>/i);

	          let labelText = label.match(/>[\S\s]*?<\//i)[0];
	          labelText = labelText.substring(1, labelText.length - 2).toUpperCase();
	          label = tagH + labelText + tagT;

	          let col = templateCols[labelIndex];
	          col = col.substring(2, col.length - 2);

	          let targetFieldSelector = '#' + col + '-field.data-field';
	          let field = $(targetFieldSelector);

	          let value = parcelRow[col];
	          let humanReadableValue = getHumanReadableValueOrNull(col, value, popupForDataSource);

	          let val;
	          if (humanReadableValue == null) {
	            val = '<p>' + value + '</p>';
	          } else if (humanReadableValue.trim() == '') {
	            val = '<p>' + value + '</p>';
	            console.warn(key, value, 'has wrong definition (e.g., unexpected value, wrong number of vals and labels, etc.)!');
	          } else {
	            val = '<p>' + humanReadableValue + '</p>';
	          }

	          parseRes += label + val;
	        }
	      }

	      //
	      // Render Leaflet popup; find your data in response.data[0]
	      //

	      // Check if popup exists
	      if($('.leaflet-popup-content').length == 0) {
	        // For the initial query results for the clicked featrue
	        // Dummy icon for a marker
	        let dummyDivIcon = L.divIcon({
	          className: 'dummy-div-icon',
	          iconSize: [0, 0]
	        });

	        // A Leaflet popup with Carto infowindow template and content
	        let popup = L.popup({
	          keepInView: true
	        })
	          .setLatLng(latlng)
	          .setContent(parseRes)
	          .openOn(this.state.map);

	        // An invisible marker to which the infowindow will be attached
	        let marker = L.marker(latlng, {
	          icon: dummyDivIcon,
	          opacity: 0
	        }).addTo(this.state.map);

	        // Append custom paragraphs; containing buttons
	        let infowindowCustomParagraphs = $('#infowindow-custom-paragraph-template').html();
	        $('.leaflet-popup-content-wrapper').append(infowindowCustomParagraphs);

	        $('.link-to-detail').click(function(e) {
	          // Fill out the form
	          renderDetailPopup(parcelRow, tableName);

	          // Make it visible
	          $('.detail-popup').modal('show');
	          e.stopPropagation();

	        });

	        marker.bindPopup(popup);
	        marker.openPopup();
	      }
	      else {
	        // For the following query results for overlapped layers
	        $('.leaflet-popup-content').append(parseRes);
	      }

	      // Render detail popup
	      renderDetailPopup(parcelRow, tableName);
	    }
	  });
	}

	_onListRowClick = ({ event, index, rowData }) => {
		this.state.map.closePopup();
		let centroidLatLng = this._getCentroidLatLngForDatapoint(rowData);
		this._setupInfoWindow(centroidLatLng, { cartodb_id: rowData.cartodb_id });
	}

	_getCentroidLatLngForDatapoint = (datapoint) => {
		let leafletGeoJson = L.geoJson(JSON.parse(datapoint.geo_json));
		let parcelPoints = leafletGeoJson.getLayers()[0].getLatLngs();
		// We get the centroid of the bounding box of the parcel, which is all the current version (0.7) of Leaflet can do
		return L.polygon(parcelPoints).getBounds().getCenter();
	}

	_setupSearchBox(mapObj) {
    if($('#map div.cartodb-searchbox').length == 0) {
      var v = cdb.vis.Overlay.create('search', mapObj.viz, {})
      v.show();
      $('#map').append(v.render().el);
    }
	}

	_updateParcelWhereClause = (clause) => {
		this.setState({
			parcelWhereClause: clause
		});
	}

	_getAndStoreMapConfig(callback) {
		getMapConfig((response) => {
			let config = JSON.parse(response.data.config);
	  	config.vizjson = JSON.parse(config.vizjson);
	  	this.setState({ config: config }, callback)
	  });
	}

	render() {
		return (
			<div className="container-fluid full-height">
		  	<div className="col col-xs-12 col-sm-8 full-height">
		  		<div className="card full-height">
			  		<div id="map" className="col col-xs-12 full-height">
	      			<MapComponent />
	      		</div>
      		</div>
      	</div>
	      <div className='parcel-list col-sm-4 hidden-xs full-height card'>
	      	<div className="col col-sm-12 full-height">
	      	{ this.state.map && this.state.cartoUserName &&
	      			<ParcelList 
					      	map={ this.state.map }
					      	cartoUserName={ this.state.cartoUserName } 
					      	setupInfoWindow={ this._setupInfoWindow } 
					      	onListRowClick={ this._onListRowClick }
					      	parcelWhereClause={ this.state.parcelWhereClause } /> }
	      	</div>
			  </div>
			<QueryUI 
			layers={ this.state.layers } 
			tables={ this.state.tables }
			updateParcelWhereClause={ this._updateParcelWhereClause } />
			</div>
			);
	}

}

ReactDOM.render(
    React.createElement(MapPage),    
    window.react_mount
  );