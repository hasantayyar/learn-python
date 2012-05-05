txt = "lorem ipsum dolor wtf"
words = txt.split(' ')
print words

sortedwords =  sorted(words)
print sortedwords

first_word = words.pop(0)
print first_word

last_word = words.pop(-1)
print last_word
