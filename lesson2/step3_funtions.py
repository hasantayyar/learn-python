def three_arg(*args):
    arg1, arg2, arg3 = args
    print "first %r\nsecond %r\nthird %r"% (arg1, arg2, arg3)

def three_arg_alt(arg1,arg2,arg3):
    print "first %r\nsecond %r\nthird %r"% (arg1, arg2, arg3)

three_arg("a1","a2","a3")
print "\nother way"
three_arg_alt("a1","a2","a3")

#### functions also can return something

def add(x,y):
    result = x + y
    return result
print "\n\n"
print add( 4, add(3,5))

