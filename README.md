# deduplicate Programming Challenge:

Take a variable number of identically structured json records and de-duplicate the set.

  

An example file of records is given in the accompanying 'leads.json'. Output should be same format, with dups reconciled according to the following rules:

1. The data from the newest date should be preferred.

2. Duplicate IDs count as dups. Duplicate emails count as dups. Both must be unique in our dataset. Duplicate values elsewhere do not count as dups.

3. If the dates are identical the data from the record provided last in the list should be preferred.

  

Simplifying assumption: the program can do everything in memory (don't worry about large files).

  

Run the `script.py` application from the command line using python. The application takes in a `leads.json` and outputs to json files: `output.json` and `removed.json`. `output.json` contains the deduplicated objects, and the `removed.json` file contains the entries removed from the final list.