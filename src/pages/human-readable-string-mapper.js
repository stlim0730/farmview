export default class HumanReadableStringMapper {

	constructor() {
		this._populateHumanReadablesMap();
	}

	_populateHumanReadablesMap() {
		this._datafieldToHumanReadables = {};
		document.querySelectorAll('.human-readability-list').forEach(readabilityEntry => { 
			let humanReadablePairs = JSON.parse(readabilityEntry.dataset.humanReadables);
			let lookup = {}
			humanReadablePairs.forEach(pair => {
				lookup[pair.val] = pair.label_eng;
			});

			this._datafieldToHumanReadables[readabilityEntry.dataset.name] = {
				lookup: lookup
			}
		});
	}

	getHumanReadableString(datafieldName, code) {
		if (datafieldName in this._datafieldToHumanReadables) {
			return this._datafieldToHumanReadables[datafieldName].lookup[code];
		} else {
			console.error("Couldn't find field name in human readable lookup.", datafieldName, this._datafieldToHumanReadables);
		}
	}

}