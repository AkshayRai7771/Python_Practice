arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
####VIMP DNF Algo
low = 0
mid = 0
high = len(arr)-1
while mid <= high:
    if arr[mid]==0:
        temp=arr[low]
        arr[low]=arr[mid]
        arr[mid]=temp
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid+=1
    elif arr[high]==2:
        high-=1
    elif arr[mid]==2 and arr[high]!=2:
        if arr[high]==1:
            temp=arr[mid]
            arr[mid]=arr[high]
            arr[high]=temp
            mid+=1
        else :
            temp=arr[high]
            arr[high]=arr[mid]
            arr[mid]=arr[low]
            arr[low]=temp
            low+=1
            mid+=1
        high-=1
print(arr)