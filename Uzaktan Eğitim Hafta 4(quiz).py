#--------------------------------------------------------------------------------------------------------------------------
'''
Min heapify: Min heap'e göre verilmiş bir array'i düzenler.(En küçük eleman kökte)
(array bir dizi tutar, i ise kontrol sırasında küçük olan elemanın indexini tutar)
Build min heap: Arraydeki tüm elamanları gönderdik.Tersten başlayacak şekilde bir dizi oluşturdu ve çağırdı.
(parametre olarak array gönderdik)
Insert ıtem to heap: Parametre olarak gönderdiğimiz elemanı heap e uygun bir şekilde ilgili yapıya ekledi.
(heapArray bir dizi tutar,key ise eklenecek olan değeri tutar)
Remove item from heap : En sonda bulunan elemanı heap yapısından sildi.
(Parametre olarak yollanan heap yapısından sondaki elemanla kökteki elemanı yer değiştirir yani en küçük elemanı siler)
Heap sort : Bir sıralama algoritması Heap yapısına göre dizideki değerleri sıralar.
(Sıralanacak olan diziyi parametre olarak göndeririz.)

'''
#--------------------------------------------------------------------------------------------------------------------------


def min_heapify(array,i):#verilen bir diziyi min heap dizilimine göre heapify eder.
    left = 2*i+1
    right = 2*i+2
    lenght=len(array)-1
    smallest = i
    if(left<= lenght and array[i] > array[left]):
        smallest=left
    if right<= lenght and array[i]>array[right]:
        smallest=right
    if smallest != i:
        array[i],array[smallest] =array[smallest], array[i]
        min_heapify(array,smallest)
        
def build_min_heap(array): #arraydeki tum elemanlar için çağırdık.Tersten başlayacak şekilde dizi oluşturur ve çağırır
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)
        
#--------------------------------------------------------------------------------------------------------------------------
def insertItemToHeap(heapArray,key):#Başta tek elemanlı ve heap durumunda,eleman eklediğimiz sürece heap durumunda ekler.
    heapArray.append(key)
    index = len(heapArray)-1
    if index<=0:
        return    
    parent = (index-1)//2
    while parent>=0 and heapArray[parent] > heapArray[index]:
        heapArray[parent],heapArray[index] = heapArray[index],heapArray[parent]            
        index = parent
        parent = (index-1)//2
    
def removeItemFromHeap(myheap):#Heap yapısında sondaki  elemanı siler.
    index = len(myheap)
    if index<=0:
        print("Heap'te eleman yok.")
        return
    myheap.pop()
#--------------------------------------------------------------------------------------------------------------------------
def heapsort(array):
    array = array.copy() #
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array

my_array_1 = [8,10,3,4,7,15,1,2,16]
build_min_heap(my_array_1)
print(my_array_1 )
insertItemToHeap(my_array_1,9)
insertItemToHeap(my_array_1,1)
removeItemFromHeap(my_array_1)
print(my_array_1 )
print(sorted(my_array_1))
