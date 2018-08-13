import axios from 'axios';

const getParcelsWithinMapBounds = (userName, mapBounds, parcelWhereClause, startIndex, endIndex, callback, errorCallback) => {
	const sql = getSqlForParcelsWithinMapBounds(mapBounds, parcelWhereClause, startIndex, endIndex);
	return makeSqlRequest(sql, userName)
			.then(response => {
				callback(response.data);
			});
}

const getParcelRowCountWithinMapBounds = (userName, mapBounds, parcelWhereClause, callback, errorCallback) => {
	const sql = getRowCountSqlForParcelsWithinMapBounds(mapBounds, parcelWhereClause);
	return makeSqlRequest(sql, userName).then(callback);
}

const makeSqlRequest = (sql, userName) => {
	const url = getUrlBase(userName) + sql;
	return axios.get(url)
		.catch(function(error) {
			console.error('error url', url)
			throw error;
		});
}

function getUrlBase(userName) {
	return `https://${ userName }.cartodb.com/api/v2/sql/?q=`;
}

function getRowCountSqlForParcelsWithinMapBounds(mapBounds, parcelWhereClause) {
	return `SELECT 1 
			FROM central_coast_joined 
			${ getWithinMapBoundsWhereClause(mapBounds, parcelWhereClause) }`;
}

function getSqlForParcelsWithinMapBounds(mapBounds, parcelWhereClause, startIndex, endIndex) {
	return `SELECT cartodb_id, the_geom, acres, sit_city, site_city, soil_type, zone_type, ST_AsGeoJSON(the_geom) AS geo_json 
			FROM central_coast_joined 
			${ getWithinMapBoundsWhereClause(mapBounds, parcelWhereClause) }
			ORDER BY cartodb_id ASC LIMIT ${endIndex + 1 - startIndex} OFFSET ${startIndex}`;
}

function getWithinMapBoundsWhereClause(mapBounds, parcelWhereClause) {
	if (mapBounds === null) {
		if (parcelWhereClause === undefined) {
			return '';
		} else {
			return 'WHERE ' + parcelWhereClause;
		}
	}
	let mapBoundsRectangle = `ST_SetSRID(ST_MakeBox2D(
			ST_Point(${ mapBounds.getWest() }, ${ mapBounds.getSouth() }), 
			ST_Point(${ mapBounds.getEast() }, ${ mapBounds.getNorth() })),
	4326)`;
	let mapBoundsClause = ` ST_INTERSECTS(${ mapBoundsRectangle }, the_geom)`;
	let maybeParcelWhereClause = '';
	if (parcelWhereClause !== undefined) {
		maybeParcelWhereClause = parcelWhereClause.replace(/</, '%3C') + ' and ';
	}
	return 'WHERE ' + maybeParcelWhereClause +  mapBoundsClause;
}

export { getParcelsWithinMapBounds, getParcelRowCountWithinMapBounds, makeSqlRequest };