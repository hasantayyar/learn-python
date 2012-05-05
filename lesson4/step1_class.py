class TheFood(object):
    def __init__(self):
        self.num = 0

    def testfunction(self):
        print "yes call me"

    def addthis(self,addthis):
        self.num += addthis
        print "oh added ", addthis

a = TheFood()
b = TheFood()

a.testfunction()
b.testfunction()

a.addthis(10)
b.addthis(20)

print a.num
print b.num
