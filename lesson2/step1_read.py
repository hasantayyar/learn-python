filename = "sample.txt"
txt = open(filename)
data = txt.read()
print "content %d bytes long " % len(data)
print data
