import React from 'react';
import ParcelList from './parcel-list';
import renderer from 'react-test-renderer';
import jquery from 'jquery';
import { List } from 'immutable';

test('getSql returns SELECT * FROM central_coast_joined', () => {
		expect(ParcelList._getSql()).toBe('SELECT * FROM central_coast_joined');
});

test('rendered component matches snapshot', () => {
	const list = List([{acres: "1"}]);
	jest.mock('jquery', () => ({
		getJSON(url, callback) {
			expect(url).toBe("https://calo1.cartodb.com/api/v2/sql/?q=");
			var res = {rows: [{acres: 1}]};
			callback(res);
		}
	}));
	const parcelList = renderer.create(
    <ParcelList cartoUserName="calo1"></ParcelList>
  );
  expect(parcelList).toMatchSnapshot();
});