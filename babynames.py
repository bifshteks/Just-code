#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
#  file = open(filename, 'r')
#  f = file.read()
#  file.close()
  with open(filename, 'r') as file:
    f = file.read
  year = re.findall(r'Popularity in (\d{4})', f)
  rnn= re.findall(
    r'<tr align="right"><td>(\d+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>',
    f)    #  rank_name(m)_name(f)

  rank_list = []
  for i in rnn:
    rank_list.append(i[1] + ' ' + i[0] + '\n')
    rank_list.append(i[2] + ' ' + i[0] + '\n')
  result = sorted(rank_list)
  result.insert(0, year[0] + r'\n')
  print(result)
  
  return result


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print ('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    for name in args:
#        filename = open(name + '.summary', w)
#        filename.write(extract_names())
#        filename.close()
      with open(name + '.summary', 'w') as filename:
        filename.write(extract_names(name))
  else:
    for name in args:
      extract_names(name)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
