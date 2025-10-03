def get_min_max(arr):
        n = len(arr)
        mini = arr[0]
        maxi = arr[n-1]
        i = 1
        while i<n:
            if arr[i]<=mini:
                  mini= arr[i]
            elif arr[i]>maxi:
                  maxi = arr[i]
            i+=1
        return(mini,maxi)

arr = [3, 2, 1, 56, 10000, 167]
min_val, max_val = get_min_max(arr)
print(min_val)
print(max_val)