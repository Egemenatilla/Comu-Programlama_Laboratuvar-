def maxOfTwo(a,b): #İki sayinın en büyüğünü veren fonksiyon
    if a>b:
        return a
    else:
        return b

def maxOfThree(a,b,c): #Üç sayının en büyüğünü veren fonksiyon
    if c > maxOfTwo(a,b):
        return c
    else:
        return maxOfTwo(a,b)

