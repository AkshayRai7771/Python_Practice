arr = [16,29,7,1,56,10]
for i in range(1,len(arr)):
    j=i-1
    val = arr[i]
    while j>=0 and val < arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=val
print(arr)
