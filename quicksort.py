from mergesort import mergeSort
import random

def main():
    arr = []
    num = 0
    with open('QuickSort_List.txt', 'r') as file:
        for line in file:
            num += 1
            arr.append(int(line))
    print(num)
    # arr = [20, 60, 30, 70, 40, 50, 10, 20, 50, 70, 5]
    # print(arr)
    # mergeSort(arr)

    # pivot_index = random.randint(0, len(arr) - 1)
    # print(arr[pivot_index])
    # result = partition(arr, 0, len(arr) - 1, pivot_index)
    # print(result)
    # print(choosePivot(arr, 0, len(arr) - 1))

    count = quickSort(arr, 0, len(arr) - 1)
    # print(arr)
    print(count)


def quickSort(arr, start, end):
    if start >= end:
        return 0
    
    # randomly choose a pivot
    pivot_index = choosePivot(arr, start, end)

    partition_index = partition(arr, start, end, pivot_index)
    # recursive calls of array with length = end - start + 1 has a total of length - 1 = end - start comparisons
    count = end - start

    count += quickSort(arr, start, partition_index - 1)
    count += quickSort(arr, partition_index + 1, end)
    return count


def choosePivot(arr, start, end):
    # randomly choose a pivot
    # pivot_index = random.randint(start, end)

    # always choose the first element
    # pivot_index = start

    # always choose the last element
    # pivot_index = end

    # take the first, middle and last element and return their median
    temp = [(arr[start], start), (arr[(end + start)//2], (end + start)//2), (arr[end], end)]
    for i in range(2):
        for j in range(2 - i):
            if temp[j][0] > temp[j + 1][0]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
    pivot_index = temp[1][1]

    return pivot_index


def partition(arr, start, end, pivot_index):

    pivot = arr[pivot_index]

    # swap the pivot element with the first element of the array
    arr[start], arr[pivot_index] = arr[pivot_index], arr[start]

    i = start + 1

    # place everything smaller or equal to the pivot on the left
    for j in range(start + 1, end + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    # swap the pivot into its rightful position
    arr[start], arr[i - 1] = arr[i - 1], arr[start]

    return i - 1
    

if __name__ == "__main__":
    main()