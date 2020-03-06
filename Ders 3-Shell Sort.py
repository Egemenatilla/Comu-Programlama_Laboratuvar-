
-----Shell Sort ile Sıralama-----

list_1=[2,5,1,6,8,6,4,9,3,0]
n = len(list_1)
gap = n // 2
while gap > 0:
    for i in range(gap, n):
        temp = list_1[i]
        j = i
        while j >= gap and list_1[j - gap] > temp:
            list_1[j] = list_1[j - gap]
            j = j - gap
        list_1[j] = temp
        print(list_1)
    gap //= 2  # --> gap = gap // 2
print(list_1)
