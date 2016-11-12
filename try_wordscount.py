
text = open('alice.txt', 'r')

read_text = text.read()
#print (read_text)
#for line in read_text:
#  line.split()
#  for word in line:
    

rext = read_text.split()
for word in rext:      #why is don't work?
  word.lower()         #
dict_1 = {word: rext.count(word) for word in rext}



text.close()
print (dict_1)


