"""
this code is made by Captain Dany
please mind your copying & pasting
I am not responsible for the theft of this document,
however, I claim ownership of this code
it's a pirate game, that's what pirates do
888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888P""  ""9888888888888888888888888888
8888888888888888P"88888P          988888"9888888888888888888
8888888888888888  "9888            888P"  888888888888888888
888888888888888888bo "9  d8o  o8b  P" od88888888888888888888
888888888888888888888bob 98"  "8P dod88888888888888888888888
888888888888888888888888    db    88888888888888888888888888
88888888888888888888888888      8888888888888888888888888888
88888888888888888888888P"9bo  odP"98888888888888888888888888
88888888888888888888P" od88888888bo "98888888888888888888888
888888888888888888   d88888888888888b   88888888888888888888
8888888888888888888oo8888888888888888oo888888888888888888888
888888888888888888888888888888888888888888888888888888888888
"""

import math
#needed for pi value

def comparator():
    #first excercise in the hw
    firstnum=int(input("Type the first number and press enter\n"))
    secnum=int(input("Type the second number and press enter\n"))
    #takes both inputs and stores them in int variables
    if(firstnum>secnum):
        print("The higher number is",firstnum)
        #takes first number as higher
    elif(secnum>firstnum):
        print("The higher number is",secnum)
        #takes second number as higher
    elif(firstnum==secnum):
        print("Both numbers are equal")
        #in case the numbers are equal
    else:
        print("Non-valid entry")
        #in case the entry is something else
    print("-------------------")
def triangle():
    triBase=float(input("Type the base\n"))
    triHeight=float(input("Type the height\n"))
    #takes input for base and height
    triAnswer=triBase*triHeight
    #stores answer in variable(decided not to do so
    #in the latter ones)
    print("The area of the triangle is", triAnswer)
    print("-------------------")
def circle():
    cirRadius=float(input("Type the radius of the circle\n"))
    #takes input for radius
    print("The area of the circle is",math.pi*cirRadius*cirRadius)
    print("-------------------")
def square():
    sideSq=float(input("Type the measure of a side of the square\n"))
    #takes input for side of square
    print("The area of the square is",sideSq*sideSq)
    print("-------------------")
def main():
    print("Select the section you want to use:")
    #takes input for menu and selection of function
    sel=int(input("1.Number comparator\n2.Triangle area\n3.Circle area\n4.Square area\n5.Exit\n"))
    if sel<=0 or sel>5:
        print("Number not valid")
        #in case someone wants to be a smarty
        main()
    elif sel==1:
        print("-------------------")
        comparator()
        main()
    elif sel==2:
        print("-------------------")
        triangle()
        main()
    elif sel==3:
        print("-------------------")
        circle()
        main()
    elif sel==4:
        print("-------------------")
        square()
        main()
    else:
        print("Exiting...")
        #exits the program
main()