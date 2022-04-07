#some notes from lesson 5
#sorting stufffff


list_of_words = ['banana', 'apple', 'orange', 'strawberry', 'book' , 'cat']
print(list_of_words)
print(sorted(list_of_words, key=len))
print(sorted(list_of_words, key=len, reverse=True))

#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = 1

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

test_array = [6, 3, 8, 1, 9, 2]
print(test_array)
print(selection_sort(test_array))


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 -i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+ 1] = arr[j +1], arr[j]
    return arr

test_array = [5, 6, 2, 9, 11, 3] #[2, 3, 5, 6, 9 ,11]
print(test_array)
print(bubble_sort(test_array))


