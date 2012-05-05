from sys  import argv

scrpit, name = argv

promt = "> "
print "hola ", name
print "what's your favourite color "
color = raw_input(promt)
print """
So 
your favourite color is %s
""" % color
