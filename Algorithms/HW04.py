'''
H4 04 - An Ninh Tran
Even First
Your input is an array of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input array).
Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

Increment a Number
Write a program that takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1.
For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].



'''

def even_first(intArray):
    new_array = []
    odd_array = []
    for n in intArray:
        if (n % 2) == 0:
            new_array.append(n)
        else:
            odd_array.append(n)

    new_array = new_array + odd_array
    print(new_array)
    return new_array




def increment_num(decimalIntegerD):
    #so everything greater then or equal to 10 is auto converted to 0? Is this right?

    #print(decimalIntegerD)
    newArray = []
    newArray.append(decimalIntegerD[0])
    #still working on this
    for n in decimalIntegerD[1:]:
        if n+1 >= 10:
            n = 0
            newArray.append(n)
        else:
            newArray.append(n+1)
    print(newArray)
    return newArray



#below are my tests to see if it works:
numberList = [5,6,7,1,2,3,4,5]
even_first(numberList)

#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

numberList = [7, 3, 5, 6, 4, 10, 3, 2]
even_first(numberList)


testInput = [1, 2, 9]
increment_num(testInput)


testInput2 = [9, 9, 9]
increment_num(testInput2)



#solutions

def even_first(arr):
    next_even, next_odd = 0, len(arr) -1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1

    return arr


print("Even first solutions:")
print(even_first(numberList))

def plus_one(arr):
    arr[-1] += 1

    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break

        arr[i] = 0
        arr[i - 1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr


print("plus one solutions:")

print(plus_one(testInput))
print(plus_one(testInput2))
