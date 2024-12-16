'''
Programming Challenge:
Take a variable number of identically structured json records and de-duplicate the set.
 

An example file of records is given in the accompanying 'leads.json'.  Output should be same format, with dups reconciled according to the following rules:
1. The data from the newest date should be preferred.
2. Duplicate IDs count as dups. Duplicate emails count as dups. Both must be unique in our dataset. Duplicate values elsewhere do not count as dups.
3. If the dates are identical the data from the record provided last in the list should be preferred.
 

Simplifying assumption: the program can do everything in memory (don't worry about large files).
 

The application should also provide a log of changes including some representation of the source record, the output record and the individual field changes (value from and value to) for each field.
'''

import json
from datetime import datetime

f = open("leads.json", "r")
data = json.load(f)
leads = data["leads"]
removed = []

def compareDates(a, b):
    date1 = datetime.fromisoformat(a)
    date2 = datetime.fromisoformat(b)
    return date1 >= date2

def removeDuplicateKeys(key, arr):
  map = {}
  for entry in arr:
    prop = entry[key]
    if prop not in map:
      map[prop] = entry      
    elif compareDates(entry["entryDate"],  map[prop]["entryDate"]):
      removed.append(map[prop])
      map[prop] = entry
  
  arr = []
  for x, y in map.items():
    arr.append(y)
  return arr

emails = removeDuplicateKeys("email", leads)
outputArr = removeDuplicateKeys("_id", emails)

outfile = open("output.json", "w")
json.dump({ "leads": outputArr }, outfile, indent=2)

removedfile = open("removed.json", "w")
json.dump({ "leads": removed }, removedfile, indent=2)

f.close()
outfile.close()
removedfile.close()