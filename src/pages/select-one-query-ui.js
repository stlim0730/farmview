import * as React from 'react';

const SelectOneQueryUI = ({ name, choices, type, data_sources_str, label_eng }) => {
	let renderedChoices = choices.map(choice => <option key={ choice.val } value={ choice.val }> { choice.label_eng } </option>);

	return (<div id={ name + '-query' } className='checkbox query-ui col-md-3'>
	  <label>
	    <input id={ name + '-checkbox' } type='checkbox' className='query-group' data-query-type={ type } data-table={ data_sources_str } data-field={ name } /> { label_eng }
	  </label>
	  <select id={ name + '-input' } className='form-control operand-ui' disabled>
	    <option value=''>- Select One -</option>
	    { renderedChoices }
	  </select>
	</div>);
}

export default SelectOneQueryUI;