#def dict_count_word(filename):
#
#  text = open(filename, 'r')
#
#  read_text = text.read()
#  rext = read_text.split()
#  for word in rext:      #why is don't work?
#    word.lower()         #
#  dict_1 = {word: rext.count(word) for word in rext}
#
#  text.close()
#

#def print_word(filename):
# 
#  dict_count_word()
#  return (dict_1)





#def print_top():
filename = 'alice.txt'
#dict_count_word()
text = open(filename, 'r')

read_text = text.read()
rext = read_text.split()
for word in rext:      #why it is don't work?
  word.lower()         #
dict_1 = {word: rext.count(word) for word in rext}
text.close()

list_value = list(dict_1.values())
list_keys = list(dict_1.keys())
#list_value_2 = list_value
#list_value_2.sort()
for i in range(20):
  for index in list_value:
    if index == max(list_value):
      print(list_keys[list_value.index(index)])
      list_value.remove(index)
      break

   


      


  
#def sth():
#  for i in list_value:
#    if i == max(list_value):
#      print(dict_1.item(i))
#      list_value.popitem(i)

#list_top_values = list_value[-20:]   # Топ-20 сортированных значений из словаря
#list_top_sort = 
#print(list_value_2)
#print(list_keys)
  

#print (list_value)
#print (list_top_values)
