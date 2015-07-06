'''
This is a command line tool to preprocess XLSForm (http://xlsform.org/) of the survey
and generate a JSON file of the form.
'''

import sys
import csv
from my_util import *

INPUT_FIELDS = ['type', 'name', 'label::English', 'label::Espa\xc3ol', 'hint::English', 'hint::Espa\xc3ol', 'required', 'constraint', 'constraint_message', 'relevant', 'default', 'appearance', 'calculation']
OUTPUT_FIELDS = ['type', 'name', 'label_english', 'label_espanol', 'hint_english', 'hint_espanol', 'required', 'constraint', 'constraint_message', 'relevant', 'default', 'appearance', 'calculation']

keys = []
questions = []

if __name__ == '__main__':
  if len(sys.argv) == 3:
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    with open(input_filename, 'rb') as csvfile:
      spamreader = csv.reader(csvfile)
      row_num = 0
      obj_cnt = 0
      for row in spamreader:
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
        obj = {}
        obj['id'] = obj_cnt
        for in_key in INPUT_FIELDS:
          index = INPUT_FIELDS.index(in_key)
          out_key = OUTPUT_FIELDS[index]
          obj[out_key] = row[index]
          if obj[out_key].startswith('select_'):
            obj[out_key] = obj[out_key].split(' ')[0]
          if out_key == 'required':
            if obj[out_key] == 'yes':
              obj[out_key] = True
            else:
              obj[out_key] = False
        # SKIP IF NO FIELD NAME
        if obj['name'] == '':
          continue
        questions.append(obj)
        obj_cnt += 1
        # END A SURVEY QUESTION
    output_json(questions, output_filename)
    print str(row_num) + ' rows processed'
    print str(len(questions)) + ' questions extracted'
  else:
    print '\nexample: $ python converter.py inputfile.csv outputfile.json\n'
