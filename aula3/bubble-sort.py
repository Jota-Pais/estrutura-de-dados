# bubble sort
def bubble_sort(a):
    for i in range (len(a)):
        for j in range (0,len(a)-i-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp    
    return a
print (bubble_sort([1,9,2,8,3,7,4,6,5]))      
    
    