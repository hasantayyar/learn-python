#!/usr/bin/python 
print("well")
print('''
well hi
and hi to you
''')
print("and so\
 go on")

age=21
name="hell"

print 'age ',age

print("age : {0}\nname:{1}".format(age,name))

print("{0:_^21}".format("hell")) # _ karakterleri ile 21 karakter olana kadar texti doldurur ve ifadeyi ortalar

print("wtf is that {yas}  -{isim}".format(yas="test",isim="test"))
print("wtf is that {yas}  -{isim}".format(yas=age,isim=name))
