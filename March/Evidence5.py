def HighAndLow(arr):
    # Initialize the highest and lowest numbers to the first element in the array
    highest = arr[0]
    lowest = arr[0]

    # Loop through the array and update the highest and lowest numbers as needed
    for num in arr:
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num

    # Return the highest and lowest numbers as a tuple
    print('The highest number is',highest)
    print('The lowest number is',lowest)
    return (highest, lowest)

def FilterEvenNumbers(arr):
    # Initialize an empty list to hold the even numbers
    even_nums = []

    # Loop through the array and add the even numbers to the new list
    for num in arr:
        if num % 2 == 0:
            even_nums.append(num)

    # Return the new list of even numbers
    print('The even numbers are', even_nums)
    return even_nums

def Average(arr):
    # Calculate the sum of the array using the built-in sum() function
    arr_sum = sum(arr)

    # Calculate the length of the array using the built-in len() function
    arr_len = len(arr)

    # Calculate the average by dividing the sum by the length
    average = arr_sum / arr_len

    # Return the average
    print('The average is',average)
    return average

def FiveChar(arr):
    # Initialize an empty list to hold the long strings
    long_strings = []

    # Loop through the array and add the long strings to the new list
    for string in arr:
        if len(string) > 5:
            long_strings.append(string)

    # Return the new list of long strings
    print('Your new array looks like this',long_strings)
    return long_strings

def AddArrays(arr1, arr2):
    # Make sure both arrays have the same length
    assert len(arr1) == len(arr2), "Arrays must have the same length"

    # Initialize an empty array to hold the results
    result = []

    # Loop through the arrays and add the corresponding elements together
    for i in range(len(arr1)):
        sum = arr1[i] + arr2[i]
        result.append(sum)

    # Return the new array of sums
    print('Your new array looks like this',result)
    return result

def ArraySetter(arrayType):
    i=0
    print('Enter your desired array size')
    arraySize=int(input())
    array=[]
    type=arrayType
    
    print('Enter the', type,'to be used in the array')
    for x in range(arraySize):
        print('Position',x)
        array.append(arrayType(input()))
    print ('Your array looks like this:', array)
    return array

exiter=False
while exiter==False:
    print('\nSelect the function you want to use\n')
    print('1. Return the highest and lowest number in an array')
    print('2. Filter the even numbers in an array')
    print('3. Return the average of numbers in an array')
    print('4. Filter the 5 characters or more strings in a list')
    print('5. Add the numbers in two arrays of the same size')
    print('0. Exit')

    selection=int(input())

    if selection==1:  
        HighAndLow(ArraySetter(int))
        
    elif selection==2:
        FilterEvenNumbers(ArraySetter(int))
        
    elif selection==3:
        Average(ArraySetter(int))
        
    elif selection==4:
        FiveChar(ArraySetter(str))
        
    elif selection==5:
        AddArrays(ArraySetter(int), ArraySetter(int))
        
    elif selection==0:
        exiter=True
        
    else:
        print('Select a valid number')