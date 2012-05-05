everything = {"name":"John", "age":25, "height":12+3+45}
print everything
everything[1] = "just test"
everything[2] = "another test"
print everything
del everything[1]
del everything[2]
print everything

########

cities = {"06":"Ankara", "34":"Istanbul", "25" : "Erzurum"}
num = "07"
if num in cities:
    print cities[num]
else:
    print "not found"

num = "06"
if num in cities:
    print cities[num]
else:
    print "not found"

