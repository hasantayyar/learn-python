#!/usr/bin/python
# look down for %r, %d, %s usage
print "more formatting"
student="cow"
lesson = 1
step = 4

#########
print "Hi %s, this is lesson %d and step%d" %(
    student,lesson,step)
print "\nI said\n"
print "Hi {0}, this is lesson {1} and step{2}".format(student,lesson,step)
#########

#########
x="hell this is lesson %d" % 1
print x
print "oh no! %r" % x
#########

#########
x = "No tidings Elven-folk have heard"
y = "Of Amroth evermore."
print x + y
#########

#########
print "_"*100 # 100 times _
#########

#########
w1 = "w"
w2 = "e"
w3 = "l"
w4 = "l"
print w1 + w2 + w3 + w4
#########


#########
# more formating exercises
formatstr = "%r %r %r %r"

print formatstr % (1,2,3,4)
print formatstr % ("well", "yeah", "great", "hell")
print formatstr % (True, True, False, True)
print formatstr % (formatstr ,formatstr ,formatstr ,formatstr ) 
#########

#########
print '''
An Elven-maid there was of old,
A shining star by day:
Her mantle white was hemmed with gold,
Her shoes of silver-grey.
'''

print """
The elven-ship in haven grey
Beneath the mountain-lee
Awaited her for many a day
Beside the roaring sea
"""




