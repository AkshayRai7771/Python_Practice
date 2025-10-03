arr = [16,29,17,1,56,10]
for i in range(0,len(arr)-1):
    val = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[val]:
            val = j 
    arr[i],arr[val]=arr[val],arr[i]#swapping after finding min element 
print(arr)