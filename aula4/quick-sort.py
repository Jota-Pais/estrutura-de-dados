def partition(array, start, end):
    p = array[end]
    i = start
    for j in range(start, end):
        if array[j] < p:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i


def quickSort(array, start, end):
    if start < end:
        position = partition(array, start, end)
        
        quickSort(array, start, position - 1)
        quickSort(array, position + 1, end)
    return array
    
    
array = [23, 27, 14, 35, 19, 42, 9]
quickSort(array, 0, len(array)-1)
print(array)
