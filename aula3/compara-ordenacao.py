import time
def bubble_sort(a):
    for i in range (len(a)):
        for j in range (0,len(a)-i-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp    
    return a
 
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

a = [10,1,9,2,8,3,7,4,6,5]


inicio_bubble = time.time()
bubble_sort(a)
fim_bubble = time.time()
tempo_decorrido_bubble = fim_bubble - inicio_bubble


inicio_insertion = time.time()
insertion_sort(a)
fim_insertion = time.time()
tempo_decorrido_insertion = fim_insertion - inicio_insertion


print("\n--- Resultados ---")
print(f"Tempo decorrido com Bubble Sort:    {tempo_decorrido_bubble:.8f} segundos.")
print(f"Tempo decorrido com Insertion Sort: {tempo_decorrido_insertion:.8f} segundos.")
print("\n--- Conclusão ---")
if tempo_decorrido_bubble < tempo_decorrido_insertion:
    print("O Bubble Sort foi mais rápido neste teste.")
else:
    print("O Insertion Sort foi mais rápido neste teste.")