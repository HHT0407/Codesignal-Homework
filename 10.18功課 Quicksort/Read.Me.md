```py
def Quicksort(list):
    smaller = []
    bigger = []
    center = []

    if len(list) <= 1:  #當list只有一個或更少元素時直接return
        return list 

    else :
        major = list[0]
        for i in list:
            if i < major:
                smaller.append(i)
            elif i > major:
                bigger.append(i)
            else : 
                center.append(i)

    smaller = Quicksort(smaller)
    bigger = Quicksort(bigger)
    return smaller + center + bigger
Terry = [13,17,19,777,20,666,26,27,34]
print ("大小順序為",Quicksort(Terry))
```
