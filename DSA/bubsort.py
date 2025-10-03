arr = [16,29,17,1,56,10]
for i in range(0,len(arr)):
    for j in range(0,len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]#swapping finding large element btw j and j+1, this will find largest element in array and will place at last index
print(arr)