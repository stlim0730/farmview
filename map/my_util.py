import simplejson as json
from simplejson import loads
import math
import time
from datetime import datetime
from random import randint
import re

# START CONSTANTS
urlRegex = re.compile(
  r'^https?://'  # http:// or https://
  r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
  r'localhost|'  # localhost...
  r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
  r'(?::\d+)?'  # optional port
  r'(?:/?|[/?]\S+)$', re.IGNORECASE)
# END CONSTANTS

# START UTILITY FUNCTIONS
def random_int(inclusiveMin, exlusiveMax):
  return randint(inclusiveMin, exlusiveMax-1)

def read_json(filename):
  return json.load(open(filename))

def output_json(obj, filename='', ind=2):
  if obj is None:
    print 'JSON object is None'
    return 1
  outputString = json.dumps(obj, sort_keys=True, indent=ind*' ')
  if filename is '':  # standard output
    print(outputString)
    return 0
  else: # output file
    if not filename.endswith('.json'):
      filename = filename + '.json'
    f = open(filename, 'w')
    f.write(outputString)
    f.close()
    return 0

def output_str(content, filename=''):
  if filename=='':
    print(content)
  else:
    f = open(filename, 'w')
    f.write(content)
    f.close()

def list_has(theList, target):
  val = binarySearch(theList, target, 0, len(theList)-1)
  if val is None:
    return False
  else:
    return True

def is_uRL(url):
  if urlRegex.match(url) is None:
    return False
  else:
    return True

def get_time_string():
  return time.strftime('%H:%M:%S')

def my_log(s):
  print '#Farmview [' + get_time_string() + '] -',
  print s
# END UTILITY FUNCTIONS
