'''
This is a command line tool to preprocess XLSForm (http://xlsform.org/) of the survey
and generate a JSON representation of query form.
'''

import sys
import csv
from my_util import *

Q_INPUT_FIELDS = ['type', 'name', 'label::English', 'label::Espa\xc3ol', 'hint::English', 'hint::Espa\xc3ol', 'required', 'constraint', 'constraint_message', 'relevant', 'default', 'appearance', 'calculation']
Q_OUTPUT_FIELDS = ['type', 'name', 'label_english', 'label_espanol', 'hint_english', 'hint_espanol', 'required', 'constraint', 'constraint_message', 'relevant', 'default', 'appearance', 'calculation']

C_OUTPUT_FIELDS = ['list_name', 'name', 'label_english', 'label_espanol', 'image']

keys = []
questions = []
choice_rows = []
choices = []

if __name__ == '__main__':
  if len(sys.argv) == 5:
    q_input_filename = sys.argv[1]
    c_input_filename = sys.argv[2]
    q_output_filename = sys.argv[3]
    c_output_filename = sys.argv[4]
    with open(c_input_filename, 'rb') as c_file: # store choices in the memeory first
      c_reader = csv.reader(c_file)
      row_num = 0
      for row in c_reader:
        row_num += 1
        # COLLECT KEYS
        if row_num == 1:
        #   keys.extend(row)
        #   keys = [key.lower() for key in keys]
          continue
        # SKIP THE EMPTY LINE
        if ''.join(row).strip() == '':
          continue
        # SKIP THE FORM NOTES
        if row[0] == 'note':
          continue
        choice_rows.append(row)
    with open(q_input_filename, 'rb') as q_file:
      q_reader = csv.reader(q_file)
      row_num = 0
      q_obj_cnt = 0
      c_obj_cnt = 0
      for row in q_reader:
        row_num += 1
        # COLLECT KEYS
        if row_num == 1:
        #   keys.extend(row)
        #   keys = [key.lower() for key in keys]
          continue
        # SKIP THE EMPTY LINE
        if ''.join(row).strip() == '':
          continue
        # SKIP THE FORM NOTES
        if row[0] == 'note':
          continue
        # SKIP THE GROUPS
        if row[0] == 'begin group' or row[0] == 'end group':
          continue
        # START A SURVEY QUESTION
        q_obj = {}
        q_obj['id'] = q_obj_cnt
        for in_key in Q_INPUT_FIELDS:
          index = Q_INPUT_FIELDS.index(in_key)
          out_key = Q_OUTPUT_FIELDS[index]
          if 'espanol' in out_key:
            q_obj[out_key] = row[index]
          else:
            q_obj[out_key] = row[index]
          if q_obj[out_key].startswith('select_'):
            out_key_splits = q_obj[out_key].split(' ')
            q_obj[out_key] = out_key_splits[0] # select_one or select_multiple
            choice_list_name = out_key_splits[1] # list name in choice input
            for c_row in choice_rows: # copy from csv to json
              if c_row[0] == choice_list_name:
                c_obj = {}
                for i in range(len(c_row)):
                  c_obj[C_OUTPUT_FIELDS[i]] = c_row[i]
                c_obj['question'] = q_obj_cnt
                c_obj['id'] = c_obj_cnt
                choices.append(c_obj)
                c_obj_cnt += 1
            # if 'or other' in q_obj[out_key]: # in case it has 'or other' option
            #   choices.append({'id': c_obj_cnt, 'question': q_obj_cnt, 'list_name': choice_list_name, 'name': 'choice_list_name' + 'other', 'label_english': 'Other', 'label_espanol': 'Other', 'image': ''})
            #   c_obj_cnt += 1
          if out_key == 'required':
            if q_obj[out_key] == 'yes':
              q_obj[out_key] = True
            else:
              q_obj[out_key] = False
        # SKIP IF NO FIELD NAME
        if q_obj['name'] == '':
          continue
        questions.append(q_obj)
        q_obj_cnt += 1
        # END A SURVEY QUESTION
    output_json(questions, q_output_filename)
    output_json(choices, c_output_filename)
    print str(row_num) + ' rows processed'
    print str(len(questions)) + ' questions extracted'
    print str(len(choices)) + ' choices extracted'
  else:
    print '\nexample: $ python converter.py question_inputfile.csv choice_inputfile.csv question_outputfile.json choice_outputfile.json\n'
    print '\nIf you have questions and choices as two sheets in a xls or xlsx file, separate them into two csv files.\n'
