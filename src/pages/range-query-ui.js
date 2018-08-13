import * as React from 'react';

const RangeQueryUI = ({ name, type, data_sources_str, label_eng }) =>
		<div id={ name + '-query' } className='checkbox query-ui col-md-3'>
		  <label>
		    <input id={ name + '-checkbox' } type='checkbox' className='query-group' data-query-type={ type } data-table={ data_sources_str } data-field={ name } />{ label_eng }
		  </label>
		  <br />
		  <input id={ name + '-min-input' } type='text' className='form-control operand-ui min-max-text-input' placeholder='Min' disabled />
		  <input id={ name + '-max-input' } type='text' className='form-control operand-ui min-max-text-input' placeholder='Max' disabled />
		</div>

export default RangeQueryUI;