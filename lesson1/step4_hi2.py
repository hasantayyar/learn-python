#!/usr/bin/python
# look down for %r, %d, %s usage
print "more formatting"
student="cow"
lesson = 1
step = 4
print "Hi %s, this is lesson %d and step%d" %(
    student,lesson,step)
print "\nI said\n"
print "Hi {0}, this is lesson {1} and step{2}".format(student,lesson,step)

x="hell this is lesson %d" % 1
print x
print "oh no! %r" % x

x = "No tidings Elven-folk have heard"
y = "Of Amroth evermore."
print x + y
