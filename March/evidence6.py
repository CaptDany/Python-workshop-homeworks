import math

"""
🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️
this code is made by 🇲🇽 Captain Dany 🇲🇽
please mind your copying & pasting
I am not responsible for the theft of this document,
however, I claim ownership of this code
it's a pirate game, that's what pirates do
🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️🏴‍☠️
"""

def temperature(value, toCelcius):
    if toCelcius==True:
        return (value-32)*5/9
    else:
        return (value * 9/5) + 32
    
def circleArea(radius):
    return radius * radius * math.pi

def vowelsOnly(string):
    vowels = "aeiouAEIOU"
    result = [char for char in string if char in vowels]
    return "".join(result)

def fillList(size):
    list=[]
    for x in range(0,size+1,1):
        list.append(input("Type the item in place {} and press Enter\n".format(x)))
    return list

def evenNum(array):
    numbers = [int(char) for char in array if char.isdigit()]
    result = [num for num in numbers if num % 2 == 0]
    return result

def main():
    print('\nSelect the function you want to use\n')
    toRun=int(input("\n1. Temperature converter\n2. Circle area from radius\n3. Return vowels only from a string\n4. Fill a list\n5. Return only even numbers\nEnter anythong else to exit\n"))
    if toRun==1:
        
        pipi=input('Convert from farenheit or celcius?\n')
        if pipi==('f' or 'farenheit' or 'F' or 'Farenheit'):
            i=True
        else:
            i=False
        
        value=int(input('Enter the temperature\n'))
        print(temperature(value,i))
        
    elif toRun==2:
        x=int(input('Enter the radius of the circle and press Enter\n'))
        print(circleArea(x))
        
    elif toRun==3:
        x=input('Type your string and press enter\n')
        print(vowelsOnly(x))
        
    elif toRun==4:
        x=int(input('Enter the size of your list\n'))
        print(fillList(x))
        
    elif toRun==5:
        x=int(input('Enter the size of your list\n'))
        print('The even numbers in your list are', evenNum(fillList(x)))
        
    else:
        return

main()
print("Exitting...")