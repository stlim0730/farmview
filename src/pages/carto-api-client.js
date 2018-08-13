import axios from 'axios';

export function getMapConfig(callback, errorCallback) {
	const url = 'config';
	axios.get(url)
			.then(callback)
			.catch(function(error) {
				errorCallback && errorCallback();
				throw error;
			});
}