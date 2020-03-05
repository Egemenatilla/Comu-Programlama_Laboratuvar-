------Selection Sort ile Sıralama------

list_1=[1,5,3,4,6,0,8,2,9,7]
print("Başlangıçta")
print(list_1)
swap_sayisi=0
for i in range(len(list_1)-1,0,-1):
    postionOfMax=0
    for j in range(1,i+1):
        if (list_1[j]>list_1[postionOfMax]):
            postionOfMax=j
    temp=list_1[j]
    list_1[j]=list_1[postionOfMax]
    list_1[postionOfMax]=temp
    swap_sayisi=swap_sayisi+1

    print("swap sayisi",swap_sayisi)
    print(list_1)

