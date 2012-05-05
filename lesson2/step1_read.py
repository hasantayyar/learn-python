filename = "sample.txt"
txt = open(filename)
data = txt.read()
print "content %d bytes long " % len(data)
print data

#########

txt = open(filename)
oneline = txt.readline()
print oneline
oneline = txt.readline()
print oneline
oneline = txt.readline()
print oneline

txt.seek(0)
oneline = txt.readline()
print oneline

