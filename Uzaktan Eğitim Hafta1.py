import random

s = random.randint(1,100)
print(s)

def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers

my_list = get_n_random_numbers(12,-100,50)       #12 tane sayı, -100 ile 50 arasından random değer.

sorted(my_list)

def my_frequency_with_dict(my_list):                        # Hash Mapping Yöntemi ile işlem yapma.
    frequency_dict={}
    for item in my_list:
        if (item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict

print(sorted(my_list))
print(my_frequency_with_dict(my_list))

def my_frequency_with_list_of_tuples(list_1):               #Liste üzerinden işlem yapma.
    frequency_list=[]
    for i in range (len(list_1)):
        s = False
        for j in range (len(frequency_list)):
            if(list_1[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return frequency_list

my_list = [2,3,4,5,3,6,3,2,2,1,3,4,5,2,3]
result_1 = my_frequency_with_dict(my_list)
result_2 = my_frequency_with_list_of_tuples(my_list)
print(result_1)
print(result_2)

my_list_1 = get_n_random_numbers(10,-5,5)
my_hist_d = my_frequency_with_dict(my_list_1)
print(my_hist_d)

my_hist_1 = my_frequency_with_list_of_tuples(my_list_1)
print(my_hist_1)

frequency_max = -1
mode = -1

for key in my_hist_d.keys():
    print(key,my_hist_d[key])
    if my_hist_d[key]>frequency_max:
        frequency_max=my_hist_d[key]
        mode = key

print(mode, frequency_max)

def my_mode_with_dict(my_hist_d):

    frequency_max=-1
    mode=-1
    for key in my_hist_d.keys():
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode = key
    return mode, frequency_max

my_mode_with_dict(my_hist_d)

my_list_100=get_n_random_numbers(10,-4,4)
my_hist_1=my_frequency_with_dict(my_list_100)
my_mode_with_dict(my_hist_1)

print(sorted(my_list_100))

my_list_1=get_n_random_numbers(10)
my_hist_list = my_frequency_with_list_of_tuples(my_list_1)
print(my_hist_list)

frequency_max = -1
mode = -1
for item,frequency in my_hist_list:
    print(item,frequency)
    if frequency>frequency_max:
        frequency_max=frequency
        mode = item
print(mode, frequency_max)

def my_mode_with_list(my_hist_list):
    frequency_max= -1
    mode = -1
    for item, frequency in my_hist_list:
        print(item,frequency)
        if frequency>frequency_max:
            frequency_max=frequency
            mode = item
    return mode,frequency_max

my_mode_with_list(my_hist_list)

my_list_100=get_n_random_numbers(20,-4,4)
my_hist_1=my_frequency_with_list_of_tuples(my_list_100)
my_mode_with_list(my_hist_1)

print(sorted(my_list_100))

def my_linear_search(my_list,item_search):              #Linear arama.
    found = (-1,-1)
    n=len(my_list)
    for indis in range(n):
        if my_list[indis]==item_search:
            found = (my_list[indis], indis)
    return found

my_list = get_n_random_numbers(10,-5,5)
print(my_list)
print(my_linear_search(my_list,3))

my_list = get_n_random_numbers(10,-5,5)
print(my_list)

s,t=0,0
for item in my_list:
    s = s+1                 #Kaç sayı var
    t = t+item              #Toplam değer
mean_= t/s                  #Ortalama hesabı
print(mean_)

def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean=t/s
    return mean

my_list = get_n_random_numbers(4,-5,5)
print(my_list)
my_mean(my_list)
print(my_mean(my_list))


n = len(my_list)                        #Bubble Sort ile sıralama
print(my_list)
for i in range(n-1,-1,-1):
    for j in range(0,i):
        if not(my_list[j]<my_list[j+1]):
            temp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = temp
print(my_list)


def my_bubble_sort(my_list):
    n = len(my_list)
    print(my_list)                      #Bubble Sort'u fonksiyon ile yapma.
    for i in range(n - 1, -1, -1):
        for j in range(0, i):
            if not (my_list[j] < my_list[j + 1]):
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

my_list = get_n_random_numbers(4,-5,5)
print(my_list)
my_bubble_sort(my_list)

def my_binary_search(my_list, item_search):                 #Binary olarak arama.
    found=(-1,-1)
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if my_list[mid] == item_search:
            return my_list[mid],mid
        elif my_list[mid] > item_search:
            high = mid - 1
        else:
            low = mid + 1
    return found

my_list_1=get_n_random_numbers(10,-10,10)
print("Liste", my_list_1)
my_list_2 = my_bubble_sort(my_list_1)
print("Sıralı liste", my_list_2)
print(my_binary_search(my_list_2,3))

size = input("Dizi boyutunu giriniz: ")
size = int(size) #convert str to int
my_list_1 = get_n_random_numbers(size)

print("Liste: ", my_list_1)

my_list_2 = my_bubble_sort(my_list_1)

print(my_list_2)
n = len(my_list_2)
if n%2 == 1:
    middle = int(n/2)+1
    median=my_list_2[middle]
    print(median)
else:
    middle_1=my_list_2[int(n/2)]
    middle_2=my_list_2[int(n/2)+1]
    median = (middle_1+middle_2)/2
    print(median)

def my_median(my_list):                                 #Medyanı bulma.
    my_list_2=my_bubble_sort(my_list_1)                 #Bubble sort ile listeyi sıralama.
    n = len(my_list_2)
    if n % 2 == 1:                                      #Tek sayı olması durumu
        middle = int(n / 2) + 1
        median = my_list_2[middle]
    else:                                               #Çift sayı olması durumu
        middle_1 = my_list_2[int(n / 2)]
        middle_2 = my_list_2[int(n / 2) + 1]
        median = (middle_1 + middle_2) / 2
    return median

my_list_2 = get_n_random_numbers(5,-10-10)
my_median(my_list_2)
