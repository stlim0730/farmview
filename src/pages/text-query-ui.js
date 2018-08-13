import * as React from 'react';

const TextQueryUI = ({ name, type, data_sources_str, label_eng }) => {
	return (
		<div id={ name + '-query' } className='checkbox query-ui col-md-3'>
		  <label>
		    <input id={ name + '-checkbox' } type='checkbox' className='query-group' data-query-type={ type } data-table={ data_sources_str } data-field={ name } />{ label_eng }
		  </label>
		  <input id={ name + '-input' } type='text' className='form-control operand-ui' placeholder='Enter text here' disabled />
		</div>);
}

export default TextQueryUI;