# Dizideki hangi elemandan kaçar tane olduğunu bulan fonksiyon
def myHistogram(liste_1,myDic):
    for i in liste_1:
        if i in myDic:
            myDic[i] = myDic[i]+1
        else:
            myDic[i] = 1
    return myDic

# Verilen degeri kadar tekrar eden deger var mı?   
def repetition(myDic,value):
    for i in myDic:
        if myDic[i]==value:
            return i
    return -1

