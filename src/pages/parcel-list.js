import * as React from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';
import Immutable from 'immutable';
import ListView from './list-view';
import { getParcelsWithinMapBounds, getParcelRowCountWithinMapBounds } from './carto-sql-client';

export default class ParcelList extends React.PureComponent {

	constructor(props) {
		super(props);
		this.state = {
			rowsLoaded: false,
			rowCountLoaded: false,
			parcelList: Immutable.List(),
			rowCount: 0,
			mapBounds: this.props.map ? this.props.map.getBounds() : null,
		};
	}

	componentDidMount() {
		this._populateRowCount();
		this._setupMapMoveListener();
	}

	componentDidUpdate(prevProps) {
		if (this.props.parcelWhereClause !== prevProps.parcelWhereClause) {
			this.setState({
				leastIndexLoading: undefined,
				greatestIndexLoading: undefined,
				leastIndexLoaded: undefined,
				greatestIndexLoaded: undefined,
				rowsLoaded: false,
				rowCountLoaded: false,
				parcelList: Immutable.List(),
				rowCount: 0
			},
			() => {
				this._populateRowCount(
				() => this.loadMoreRows({ startIndex: this.state.mostRecentStartIndex, stopIndex: this.state.mostRecentStopIndex }));
			});
		}
	}

	loadMoreRows = ({ startIndex, stopIndex }) => {
		//console.log(`Loading rows ${startIndex} to ${stopIndex}.`);
		this.setState({
			mostRecentStartIndex: startIndex,
			mostRecentStopIndex: stopIndex
		});

		if (!this._shouldLoadAnything(startIndex, stopIndex)) {
			return Promise.resolve();
		}

		let unloadedStartIndex = startIndex;
		let unloadedStopIndex = stopIndex;
		if (!this._nothingLoaded()) {
			if (this._loadingAbove(stopIndex)) {
				unloadedStartIndex = this.state.greatestIndexLoading + 1;
			} else {
				unloadedStopIndex = this.state.leastIndexLoading - 1;
			}
		}

		let greatestIndexLoading, leastIndexLoading;
		if (this.state.greatestIndexLoading) {
		  greatestIndexLoading = Math.max(this.state.greatestIndexLoading, unloadedStopIndex);
		} else {
			greatestIndexLoading = unloadedStopIndex;
		}

		if (this.state.leastIndexLoading) {
		  leastIndexLoading = Math.min(this.state.leastIndexLoading, unloadedStartIndex);
		} else {
			leastIndexLoading = unloadedStartIndex;
		}

		this.setState({
				leastIndexLoading: leastIndexLoading,
				greatestIndexLoading: greatestIndexLoading,
			});

		//console.log(`Loading rows ${unloadedStartIndex} to ${unloadedStopIndex}.`);
		return getParcelsWithinMapBounds(
			this.props.cartoUserName,
			this.state.mapBounds,
			this.props.parcelWhereClause,
			unloadedStartIndex,
			unloadedStopIndex,
			response => {
				const newList = this.state.parcelList.splice(unloadedStartIndex, response.rows.length, ...response.rows);
				this.setState({
					parcelList: newList,
					rowsLoaded: true,
					greatestIndexLoaded: Math.max(this.state.greatestIndexLoaded, unloadedStopIndex),
					leastIndexLoaded: Math.min(this.state.leastIndexLoaded, unloadedStartIndex)
				});
	    },
	    () => { });
	}

	_nothingLoaded = () => {
		return this.state.greatestIndexLoaded === undefined && this.state.leastIndexLoaded === undefined;
	}

	_loadingAbove = (stopIndex) => {
		return stopIndex > this.state.greatestIndexLoading;
	}

	_shouldLoadAnything = (startIndex, stopIndex) => {
		return this.state.leastIndexLoading === undefined || this.state.greatestIndexLoading === undefined || 
			startIndex < this.state.leastIndexLoading || stopIndex > this.state.greatestIndexLoading;
	} 

	isRowLoaded = (ind) => {
		const { parcelList } = this.state;
		//console.log(`isRowLoaded ${ind} ${!!parcelList[ind]}`);
		return !!parcelList[ind];
	}

	_setupMapMoveListener = () => {
		this.props.map.on('movestart', event => 
			this.setState({ 
				rowsLoaded: false,
				rowCountLoaded: false
			}));
		this.props.map.on('moveend', event => {
			this.setState({
				mapBounds: this.props.map.getBounds(),
			});
			this._resetRowLoadingMemoization(
				() => this._populateRowCount(
					() => this.loadMoreRows({ startIndex: this.state.mostRecentStartIndex, stopIndex: this.state.mostRecentStopIndex })));
		});
	}

	_resetRowLoadingMemoization = (callback) => {
		this.setState({
			greatestIndexLoaded: undefined,
			leastIndexLoaded: undefined,
			leastIndexLoading: undefined,
			greatestIndexLoading: undefined,
			leastIndexLoaded: undefined,
			greatestIndexLoaded: undefined
		}, callback)
	}

	_populateRowCount = (callback) => {
		getParcelRowCountWithinMapBounds(
			this.props.cartoUserName,
			this.state.mapBounds,
			this.props.parcelWhereClause,
			response => {
				this.setState({ 
					rowCountLoaded: true,
					rowCount: response.data.rows.length,
					parcelList: Immutable.List()
				}, () => this.listViewRef.infiniteLoaderRef.resetLoadMoreRowsCache());
				//console.log('Fetched the row count.');
				typeof callback === 'function' && callback();
    	},
    	() => {});
	}

	render() {
		return (
			this.props.cartoUserName && <ListView 
					ref={(instance) => this.listViewRef = instance}
					isRowLoaded={ this.isRowLoaded }
					loading={ !this.state.rowsLoaded || !this.state.rowCountLoaded }
					loadMoreRows={ this.loadMoreRows }
					parcelList={ this.state.parcelList } 
					rowCount={ this.state.rowCount }
					onListRowClick={ this.props.onListRowClick } />
			);
	}

}