# divide o problema em sub-problemas, divide o vetor continuamente pela metade até as unidades e ordena ao juntar as metades continuamente
def mergeSort(a):
    if len(a) > 1:
        half = len(a) // 2 
        left = a[:half]
        right = a[half:]

        mergeSort(left)
        mergeSort(right)     
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    return a

result = mergeSort([23, 27, 14, 35, 19, 42, 9])
print(result)
