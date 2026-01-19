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
