arr = [2, 3, -8, 7, -1, 2, 3]
sum = 0
maxi = max(arr)
for i in range(0,len(arr)):
    sum+= arr[i]
    if maxi<sum:
        maxi = sum 
    elif sum < 0:
        sum = 0
print(maxi) 