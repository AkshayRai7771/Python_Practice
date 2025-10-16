# l = [1,2,5,5,5,5,5,5,7]
# x = 5
# ans = []
# res = -1
# #first 
# left = 0
# right = len(l)-1
# while left<=right:
#     mid = int((left+right)/2)
#     if l[mid]==x:
#         res = mid
#         right = mid -1 
#     elif l[mid]>x:
#         right = mid-1
#     elif l[mid]<x:
#         left = mid+1
# ans.append(res)
# #last
# left=0
# right=len(l)-1
# while left<=right:
#     mid = int((left+right)/2)
#     if l[mid]==x:
#         res = mid
#         left = mid +1 
#     elif l[mid]>x:
#         right = mid-1
#     elif l[mid]<x:
#         left = mid+1
# ans.append(res)
# print(ans)




# #brute 
# # while left=<right:
# #     if l[left] == l[right] == x:
# #         res.append(left)
# #         res.append(right)
# #         break
# #     elif l[left]!=x:
# #         left+=1
# #     elif l[right]!=x:
# #         right-=1

# # print(res)

nums =[4,5,6,7,0,1,2]
#finding min element
# n = len(nums)
# left = 0
# right = n-1
# x = 5
# ans = -1
# while left <= right :
#     mid = int((left+right)/2)
#     nex = (mid+1)%n
#     pre = (mid+n-1)%n 
#     if nums[mid]<nums[nex] and nums[mid]<nums[pre]:
#         i = mid 
#         break
#     elif nums[mid]<nums[right]:
#         right=mid-1
#     elif nums[mid]>nums[left]:
#         left = mid+1
target =  3
left, right = 0, len(nums) - 1
ans = -1
while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        ans =  mid
        break

    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1


print(ans)