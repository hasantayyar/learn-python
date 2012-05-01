#!/usr/bin/python 
num = 23
goon=True

while goon :
    inp = int(input("give me a number "))
    if inp==num:
        print("WTF!! you guessed!")
        goon=False
    elif inp<num:
        print("too close but it is bigger")
    else:
        print("too close but it is smaller")
