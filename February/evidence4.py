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
def function1():
    for i in range(1, 11):
        print(i)
def function2():
    sum = 0
    i = 1

    while i <= 100:
        sum += i
        i += 1
        print("The sum this far is",sum)

    print("The sum of numbers from 1 to 100 is:", sum)
def function3():
    value = int(input("Enter the number of values: "))
    total = 0

    for i in range(value):
        num = int(input(f"Enter number {i+1}: "))
        total += num

    average = total / value
    print("The average is:", average)
def function4():
    string = input("Enter a string: ")

    for char in string:
        print(char)
def function5():
    num = int(input("Enter a number: "))
    factorial = 1

    for i in range(1, num+1):
        factorial *= i

    print("The factorial of", num, "is", factorial)
def function6():
    arr = input("Enter an array of numbers, separated by spaces: ")
    arr = list(map(int, arr.split()))

    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    print("The largest number in the array is:", largest)
def function7():
    string = input("Enter a string: ")
    vowels = "aeiouAEIOU"

    count = 0

    for char in string:
        if char in vowels:
            count += 1

    print("The number of vowels in the string is:", count)
def function8():
    for i in range(1, 1001):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
def function9():
    for i in range(1, 11):
        for j in range(1, 11):
            product = i * j
            print(f"{i} x {j} = {product}")
        print()
def function10():
    optionChosen=int(input("Choose an option from the list:\n \n1.Area of a triangle\n2.Area of a square\n3.Area of a circle\n4.Area of a pentagon\nAny other key and ENTER to exit."))
    if optionChosen==1:
        base=float(input("Enter the base: "))
        height=float(input("Enter the height"))
        print("Area of the triangle equals",base*height/2)
    elif optionChosen==2:
        side=float(input("Enter the lenght of a side: "))
        print("Area of the square equals",side*side)
    elif optionChosen==3:
        radius=float(input("Enter the radius: "))
        area = math.pi * radius ** 2
        print("Area of the circle is",area)
    elif optionChosen==4:
        side_length = float(input("Enter the side length of the pentagon: "))
        area = (5/4) * side_length ** 2 * (1 / math.tan(math.pi/5))
        print("The area of the pentagon is:", area)
    else:
        print("Exiting...")

toRun=1
while toRun>0 and toRun<11:
    print("Choose the option you want to run:\n1.Print the numbers from 1 to 10 with a for loop\n2.Print the sum of the numbers from 1 to 100 using a while loop\n3.Print the average of n numbers using a loop to\n4.Print a string letter by letter\n5.Print the factorial of a number\n6.Print the largest number among n numbers\n7.Print the number of vowels, in a string\n8.Print the numbers from 1 to 1000 that are divisible by 3 and 5\n9.Print the tables from 1 to 10 using only two cycles\n10.Area of shapes\nPress any other key to exit")
    toRun=int(input("\nType number and press enter\n"))
    if toRun==1:
        function1()
    elif toRun==2:
        function2()
    elif toRun==3:
        function3()
    elif toRun==4:
        function4()
    elif toRun==5:
        function5()
    elif toRun==6:
        function6()
    elif toRun==7:
        function7()
    elif toRun==8:
        function8()
    elif toRun==9:
        function9()
    elif toRun==10:
        function10()
print("Exiting...")