```py
def Quicksort(list):
    smaller = []
    bigger = []
    keylist = []

    if len(list) <= 1:
        return list

    else :
        key = list[0]
        for i in list:
            if i < key:
                smaller.append(i)
            elif i > key:
                bigger.append(i)
            else : 
                keylist.append(i)

    smaller = Quicksort(smaller)
    bigger = Quicksort(bigger)
    return smaller + keylist + bigger
Terry = [13,17,19,777,20,666,26,27,34]
print("大小順序是",Quicksort(Terry))
```
