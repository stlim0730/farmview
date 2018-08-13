import * as React from 'react';

export default class SelectMultipleQueryUi extends React.PureComponent {

  _resetChoices = () => {
    let checkboxes = $('#' + this.props.name + '-choices').find('input');
    let vals = [];
    for (let i = 0; i < checkboxes.length; i++) {
      let checkbox = $(checkboxes[i]);
      checkbox.prop('checked', false)
    }
    $('#' + this.props.name + '-input').val('No values selected');
  }

  _cancelChoices = () => {
    var current = $('#' + this.props.name + '-checkbox').prop('checked');
    $('#' + this.props.name + '-checkbox').prop('checked', !current);

    var vals = $('#' + this.props.name + '-input').val().split(',');

    var checkboxes = $('#' + this.props.name + '-choices').find('input');
    for (var i = 0; i < checkboxes.length; i++) {
      var checkbox = $(checkboxes[i]);
      checkbox.prop('checked', false)
    }

    for (var i = 0; i < vals.length; i++) {
      $('#' + choices_id).find('input[data-val="' + vals[i] + '"]').prop('checked', true);
    }
  }

  _applyChoices = () => {
    var checkboxes = $('#' + this.props.name + '-choices').find('input');
    var vals = [];
    for (var i = 0; i < checkboxes.length; i++) {
      var checkbox = $(checkboxes[i]);
      if (checkbox.prop('checked')) {
        var val = checkbox.data('val');
        vals.push(val);
      }
    }

    if (vals.length == 0) {
      this._resetChoices();
      $('#' + this.props.name + '-checkbox').prop('checked', false);
    }
    else {
      $('#' + this.props.name + '-input').val(vals.join());
      $('#' + this.props.name + '-checkbox').prop('checked', true);
    }
  }

  render() {
    let renderedChoices = this.props.choices.map(choice => {
      return (<li key={ choice.val } className='list-group-item'>
              <label>
                <input id={ choice.val + '-checkbox' } type='checkbox' data-val={ choice.val }/>
                { choice.label_eng }
              </label>
            </li>);
    });

    return (
      <div id={ this.props.name + '-query' } className='checkbox query-ui col-md-3'>
        <label>
          <input id={ this.props.name + '-checkbox' } type='checkbox' className='query-group' data-query-type={ this.props.type } data-table={ this.props.data_sources_str } data-field={ this.props.name } data-toggle='collapse' data-target={ '#' + this.props.name + '-choices' } />{ this.props.label_eng }
        </label>
        <input id={ this.props.name + '-input' } type='text' className='form-control operand-ui col-md-2 output-only' placeholder='No values selected' disabled />
        <div id={ this.props.name + '-choices' } className='collapse bottom-fixed-popup'>
          <ul className='list-group'>
            { renderedChoices }
            <li className='list-group-item'>
              <div className='btn-toolbar'>
                <div className='btn-group'>
                  <div type='button' className='btn btn-default' data-toggle='collapse' data-target={ '#' + this.props.name + '-choices' } onClick={ this._cancelChoices }>Cancel</div>
                  <div type='button' className='btn btn-default' onClick={ this._resetChoices }>Reset</div>
                  <div type='button' className='btn btn-primary' data-toggle='collapse' data-target={ '#' + this.props.name + '-choices' } onClick={ this._applyChoices }>Apply</div>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>);
  }

}

          // START SELECT-MULTIPLE QUERY UI
          // $('button.apply-selection').click(function (e) {
          //   var query_ui_id = $(this).closest('div.query-ui').attr('id');
          //   var field_name = query_ui_id.substring(0, query_ui_id.length - '-query'.length);
          //   var vals = [];
          //   var modal_content = $(this).closest('div.modal-content');
          //   var checkboxes = modal_content.find('input[type=checkbox].operand-ui');
          //   for (var i = 0; i < checkboxes.length; i++) {
          //     var checkbox = checkboxes[i];
          //     if (checkbox.checked) {
          //       vals.push(checkbox.value);
          //     }
          //   }
          //   var val_str = vals.join(); // JOIN WITH COMMA BY DEFAULT
          //   $('#' + field_name + '-input').val(val_str);
          //   $('button.close').click();
          // });
          // END SELECT-MULTIPLE QUERY UI