def binarysearch(array,value):
    lo = 0
    hi = len(array)-1
    while(lo<=hi):
        mid = lo + (hi-lo)//2
        if(value<array[mid]):
            hi = mid - 1
        elif(value>array[mid]):
            lo = mid + 1
        else:
            return mid
x = binarysearch(list(range(285)),3)
y = binarysearch(list(range(285)),290)
print(x)  #prints 3
print(y)  #prints none