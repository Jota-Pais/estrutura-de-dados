def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        temp = a[i]
        j = i-1
        while j >= 0 and temp < a[j] :
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
    return a
print(insertion_sort([1,9,2,8,3,7,4,6,5]))
