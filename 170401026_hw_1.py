list =[]
list2=[]
my_d = dict()
def Maxhis(my_d,str):
    deger =""
    mnum = 0
    for kelime in my_d:
        num = int(my_d[kelime])
        index = kelime.find(str)

        if num > mnum and index == 0:
            mnum = num
            deger = kelime


    return deger

def countstr(str):

    scount = 0

    for c in str:

        if c==' ':
            scount +=1

    return scount+1



def complist(list_1,height):
    list_2 =[]
    for i in range(0,len(list_1)-height+1):
        str =""

        for k in range(i, i + height):
            str2=list_1[k]

            str += str2
            str += ' '

        list_2.append(str)

    return list_2

def my_h(list_1):

    my_d = dict()

    for i in list_1:

        if i in my_d:
            my_d[i] += 1

        else:
            my_d[i] = 1


    return my_d


def file_txt():
    with open("file.txt","w") as dosyalar:

        for i in range(1,11):
            a=str(i)
            file=open(a+".txt","r")
            for satir in file:
                dosyalar.write(satir)
            dosyalar.write("\n")
            file.close()

file_txt()

with open("input.txt","r") as dosyainput: # programı baslatmadan önce lütfen input.txt dosyasını dizine atınınız
    with open("output.txt", "w") as dosyaoutput:
        for inputsatir in dosyainput:
            num = countstr(inputsatir)
            if inputsatir.endswith("\n"):
                inputsatir = inputsatir.replace("\n","")
            list2.clear()

            dosyalar = open("file.txt", "r")
            for satir in dosyalar:
                list.clear()
                for kelime in satir.split(" "):
                    list.append(kelime)
                if num <= 5:
                    list2.extend(complist(list, num+1))
            dosyalar.close()

            my_d = my_h(list2)

            if num <= 5:
                tahmin = Maxhis(my_d,inputsatir)
            else:
                tahmin = "Hatalı girdi lütfen en fazla 5 kelimelik cümle giriniz"

            dosyaoutput.write(tahmin+"\n")

    print("Sonuclara output.txt dosyasında")
