import * as React from 'react';

const ProximityQueryUI = ({ name, data_sources_str, type }) => 
<div id={ name + '-query' } className='checkbox query-ui col-md-6'>
  <label>
    <input id={ name + '-checkbox' } type='checkbox' className='query-group' data-table={  data_sources_str } data-query-type={ type } data-field={ name } />Within 
  </label>
  <br />
  <input id={ name + '-distance-input' } type='text' className='form-control operand-ui proximity-distance-text-input' placeholder='Maximum Distance' disabled /> miles of 
  <input id={ name + '-location-input' } type='text' className='form-control operand-ui proximity-location-text-input' placeholder='Location (for example, an address or a city)' disabled />
</div>

export default ProximityQueryUI;