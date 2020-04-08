import sys
import csv

def frequency_with_dict(list):
    frequency_dict={}
    for item in list:
        if item in frequency_dict:
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict

def mean_of_list(liste):
    toplam=0
    s=0
    for item in liste:
        toplam+=int(item)
        s+=1
    return int(toplam/s)

def my_median(liste):
    liste2=bubble_sort(liste)
    n=len(liste2)
    if n%2 == 1:
        middle = int(n/2)
        median = liste2[middle]
    else:
        middle1 = liste2[int(n/2)-1]
        middle2 = liste2[int(n/2)]
        median = (middle1+middle2)/2
    return median

def mode_with_dict(my_dict):
    frequency_max = -1
    mode = -1
    for key in my_dict.keys():
        if my_dict[key] > frequency_max:
            frequency_max = my_dict[key]
            mode = key
    return mode,frequency_max

def bubble_sort(liste):

    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if liste[j] > liste[j+1]:
                temp = liste[j]
                liste[j]=liste[j+1]
                liste[j+1] = temp

    return liste



with open(sys.argv[1]+"/input_hw_2.csv","r") as file:
    content = file.read()
    i=0
    insan = content.split(";")
    date = []
    for i in range(3,len(insan),3):
        date.append(insan[i].split("-"))
    
    #print(date[0][1])
    fired_month = []
    for i in range(len(date)):
        fired_month.append(date[i][1])
        
    frequency_month = frequency_with_dict(fired_month)
    
            
print(frequency_month)
print()

a = mode_with_dict(frequency_month)
numbers = []
for i,j in frequency_month.items():
    numbers.append(j)

numbers1= bubble_sort(numbers)

with open(sys.argv[2]+"/170401026_hw_2_output.txt","w") as file:
    x = my_median(numbers1)
    file.write("Medyan"+" "+str(x)+"\n")
    file.write("Ortalama"+" "+str(mean_of_list(numbers1)))