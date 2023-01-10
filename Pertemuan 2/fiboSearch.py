def fib(n):
    if n < 1 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

def Fibonaccisearch(arr,x):
    n = 0
    while fib(n) < len(arr):
        n = n + 1
    offset = -1
    while (fib(n) > 1):
        i = min(offset + fib(n-2), len(arr) - 1)
        print("Current Element : ",arr[i])
        if (x > arr[i]):
            n = n -1
            offset = i
        elif (x < arr[i]):
            n = n - 2
        else :
            return i
    if(fib(n-1) and arr[offset + 1] == x):
        return offset + 1
    return -1

arr = [1,4,8,11,13,17,21,22,23,25,28]
x = 17
print("Number found at index : ",Fibonaccisearch(arr,x))