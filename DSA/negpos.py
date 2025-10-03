arr = [1, -1, 3, 2, -7, -5, 11, 6 ]
arr1 =[]
arr2=[]
for i in range (0,len(arr)):
    if arr[i]<0:
        arr2.append(arr[i])
    else : arr1.append(arr[i])
del arr[0:]
arr.extend(arr1)
arr.extend(arr2)
print(arr)