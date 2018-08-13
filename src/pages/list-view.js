import Immutable from 'immutable';
import * as React from 'react';
import PropTypes from 'prop-types';
import { InfiniteLoader, Column, Table, AutoSizer } from 'react-virtualized';
import HumanReadableStringMapper from './human-readable-string-mapper';
import PulseLoader from './pulse-loader';

export default class ListView extends React.PureComponent {

	componentDidMount() {
		this.setState({
			humanReadableStringMapper: new HumanReadableStringMapper()
		})
	}

	componentDidUpdate() {
		this.infiniteLoaderRef && this.infiniteLoaderRef.forceUpdate();
	}

	render = () => {
		const rowGetter = ({index}) => this._getDatum(this.props.parcelList, index);

		const headerRenderer = ({ columnData,
		  dataKey,
		  disableSort,
		  label,
		  sortBy,
		  sortDirection }) => label;

		return (
			<div style={{ height : "100%" }}>
				<div className="parcel-list-title">showing { this.props.loading && <PulseLoader contents="__" /> || this.props.rowCount } parcels</div>
				<InfiniteLoader
				ref={ (instance) => this.infiniteLoaderRef = instance }
				isRowLoaded={ this.props.isRowLoaded }
				loadMoreRows={ this.props.loadMoreRows }
				rowCount={ this.props.rowCount }
				threshold={ 60 }
				minimumBatchSize={ 40 }>
					{({onRowsRendered, registerChild}) =>
					(
					<AutoSizer>
					{({ width, height }) => (
						<Table
		          ref={ registerChild }
							headerHeight={ 35 }
							headerRenderer={ headerRenderer }
							height={ height - 23 }
							hideIndexColumn
							list={ this.props.parcelList }
							onRowClick={ this.props.onListRowClick }
							onRowsRendered={ onRowsRendered }
							rowCount={ this.props.rowCount }
							rowGetter={ rowGetter }
							rowHeight={ 30 }
							width={ width }>
							<Column
				        label="Acres"
				        cellDataGetter={({ rowData }) => rowData.acres}
				        dataKey="acres"
				        width={ width * 0.13 } />
							<Column
				        label="Location"
				        cellDataGetter={({ rowData }) => Object.keys(rowData).length === 0 ? '' : rowData.sit_city || this._capitalizeCityName(rowData.site_city) || "Not Listed"}
				        dataKey="sit_city"
				        width={ width * 0.20 } />
							<Column
				        label="Zoning"
				        cellDataGetter={({ rowData }) => this.state.humanReadableStringMapper.getHumanReadableString('zone_type', rowData.zone_type)}
				        dataKey="zone_type"
				        width={ width * 0.37 } />
							<Column
				        label="Soil"
				        cellDataGetter={({ rowData }) => this.state.humanReadableStringMapper.getHumanReadableString('soil_type', rowData.soil_type)}
				        dataKey="soil_type"
				        width={ width * 0.30 } />
			      </Table>
			      )}
					</AutoSizer>
				)}
				</InfiniteLoader>
			</div>
			);
	}

  _getDatum(list, index) {
    return list.get(index, {});
  }

  _capitalizeCityName(cityName) {
  	if (!cityName) {
  		return undefined;
  	} else {
  		cityName.trim()
	  	.split(' ')
	  	.map(cityWord => {
	  		if (!cityWord || cityName.length == 0) {
		  		return cityWord;
		  	} else {
		  		cityWord[0].toUpperCase() + cityWord.slice(1).toLowerCase();
		  	}
		  }).join('');
  	}
	}

}

ListView.propTypes = {
	isRowLoaded: PropTypes.func.isRequired,
	loading: PropTypes.bool.isRequired,
	loadMoreRows: PropTypes.func.isRequired,
  parcelList: PropTypes.instanceOf(Immutable.List).isRequired,
  rowCount: PropTypes.number.isRequired,
};
