
# -----Bubble Sort İle Sıralama-----

list_1=[2,5,3,6,26,84,1,67]
print("Sıralamadan önce")
print(list_1)
for i in range(len(list_1)-1,0,-1):
  for j in range(i):
    if(list_1[j]>list_1[j+1]):
      t=list_1[j]
      list_1[j]=list_1[j+1]
      list_1[j+1]=t
print("Sıralamadan sonra")
print(list_1)
