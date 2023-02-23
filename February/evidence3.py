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

def BiggestNum():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a==b and a==c and b==c:
        print("All numbers are equal.")
    else:
        if a > b and a > c:
            print("The largest number is:", a)
        elif b > a and b > c:
            print("The largest number is:", b)
        else:
            print("The largest number is:", c)

def DivYear():
    year = int(input("Enter a year: "))

    if year % 100 == 0:
        print(year, "is divisible by 100")
    elif year % 2 == 0:
        print(year, "is even")
    else:
        print(year, "is neither even nor divisible by 100")

def Grade():
    grade1 = float(input("Enter grade 1: "))
    grade2 = float(input("Enter grade 2: "))
    grade3 = float(input("Enter grade 3: "))

    average = (grade1 + grade2 + grade3) / 3

    if grade3 < 7 or average < 7:
        print("You have failed the course with an average of", average)
    else:
        print("You have passed the course with an average of", average)

choiceA=input("Would you like to run the first function? y/n\n")
if choiceA[1]=="y" or choiceA[1]=="Y":
    BiggestNum()
else:
    choiceA
choiceB=input("Would you like to run the second function? y/n\n")
if choiceB[1]=="y" or choiceB[1]=="Y":
    DivYear()
else:
    choiceB
choiceC=input("Would you like to run the third function? y/n\n")
if choiceC[1]=="y" or choiceC[1]=="Y":
    Grade()
else:
    choiceC