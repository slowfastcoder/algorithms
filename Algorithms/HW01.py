#An Tran
#Algorithms HW 1
#3/10/2022


def main():
    if __name__== "__main__" :
        print(add_sum(5))
        print("test")


#Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
def add_sum(num):
    _n = 0
    n = 0;

    while _n < num:
        _n += 1
        n += _n
        print(f"counter value: {_n} sum value:{n}")

    return n


#Find max number from 3 values, entered manually from a keyboard.
#Example: 124, 21, 32. Result = 124.
def find_max(*args):
    y = max(*args)
    return y

#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
def count_odd_even(number):
    stringNum = str(number)
    number_length = len(stringNum)
    print(f"length of Number = {number_length}")

    evenCounter = 0
    oddCounter = 0

    for f in stringNum:
        if (int(f) % 2) == 0:
            evenCounter += 1
        else:
            oddCounter += 1

    message = "There are " + str(evenCounter) + " even numbers and " + str(oddCounter) + " odd numbers" + " within " + stringNum
    return message



print("Sum test")
add_sum(5)
add_sum(3)


print("Max Test")
print(find_max(1,10,3,20))


print("Count odd and event test")
print(count_odd_even(123456789))
print(count_odd_even(55555222))
print(count_odd_even(999999999666666))