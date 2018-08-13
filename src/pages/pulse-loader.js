import * as React from 'react';

export default class PulseLoader extends React.PureComponent {

	render() {
		return (<span className="pulse-loader">{ this.props.contents }</span>);
	}

}