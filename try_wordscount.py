def print_word(filename):
  def dict_count_word():

    text = open(filename, 'r')

    read_text = text.read()
    rext = read_text.split()
    for word in rext:      #why is don't work?
      word.lower()         #
    dict_1 = {word: rext.count(word) for word in rext}

    text.close()

  print (dict_1)
