#HW 5 - An Ninh Tran 4/6/22
'''
Selection Sort
Implement the selection sort algorithm that is sorting in descending order.

Bubble Sort
Implement the bubble sort algorithm that is sorting in descending order.

Insertion Sort
Implement the insertion sort algorithm that is sorting in descending order.

Merge Sort
Implement the merge sort algorithm that is sorting in descending order.


'''

#to reverse the array just use .sort(reverse=True) when it is done
# you can also use the built in sorted method: sorted(list, reverse=True)

#these are the same sort algorithms from algorithms lesson 5
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range( i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    #reverse it
    arr = sorted(arr, reverse=True)
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 -i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+ 1], arr[j]
    #reverse it
    arr = sorted(arr, reverse=True)
    return arr

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    #reverse it
    arr = sorted(arr, reverse=True)
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    arr = merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))
    #reverse it
    arr = sorted(arr, reverse=True)
    return arr

def merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] <= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(left_arr[i])
            i += 1

    return merged_array




#practice tests
test_array = [4, 2, 6, 1, 8, 9] #1,2,4,6,8,9

print("selection sort test")
print(selection_sort(test_array))

print("bubble sort test")
print(bubble_sort(test_array))
print("bubble sort test - reversed")

print(sorted(bubble_sort(test_array), reverse=True))

print("Insertion sort test")
y = insert_sort(test_array)
print(y)
y.sort(reverse=True)
print(y)

print("merge sort test")
test_array = [4, 8, 2, 1, 9,6]
#print(test_array)
y = merge_sort(test_array)
print(y)
y.sort(reverse=True)
print(y)



