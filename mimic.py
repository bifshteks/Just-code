#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  filename_ = open(filename, 'r')
  text_read = filename_.read()
  filename_.close()
  
  text = text_read.split()   # list
  text.append('qwerty')

#  text_not_re = text
#  for i in text_not_re:
 #   if text_not_re.count(i) > 1:
#      text_not_re.remove(i)
#  words_follow = dict.fromkeys(text_not_re[:20])  # удалить срез
  txt = set(text)
  mim_dict = {}
  mim_dict.fromkeys(text)
  for word in text:
    if word != 'qwerty':
      mim_dict[word] = text[text.index(word) + 1]  # будет перезаписываться 
                                                   # значение
  list_md = list(mim_dict)

#  for key, value in mim_dict:
#    if list_md.count(key) > 1:       #list_md = 
                                             #[(word , 1), (word2 , 2)]
  for item in list_md:
    while list_md[0].count(item) > 1:
      list_md[1] += ',' + list_md[    list_md[      list_md.index(item,[list_md.index(item)+ 1,])    ][1]    ] # добавляет в [1] значение из словаря ключа, который встречается в срезе, следующим за индексом этого 
      i = list_md.index(item,[list_md.index(item)+ 1,])   # удаляет этоу самую следующую пару
      list_md.remove(list_md[i])                          # 
    
      
  






                                                  # text[text.index(word) + 1]

  
  print(mim_dict)  
  return


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print ('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()


