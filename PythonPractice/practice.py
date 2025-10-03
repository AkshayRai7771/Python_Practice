from collections import Counter
#Merging and sorting the lists 

# a1 = [2,5,8,12,15]
# a2 = [1,3,9,11,13]
# a3 = a1 + a2
# for i in range (0,len(a3)):
#    for j in range (i+1,len(a3)):
#        if (a3[i]>a3[j]):
#            x = a3[i]
#            a3[i]=a3[j]
#            a3[j]=x
        
# print(a3)

# l1 = [8,9,0,3]
# l2 = [2,6,4,7]
# l = l1 + l2
# for i in range (0,len(l)):
#     for j in range (i+1,len(l)):
#         if (l[i]>l[j]):
#             x = l[i]
#             l[i]=l[j]
#             l[j]=x
# print(l)

# arr1= [10, 5, 15] 
# arr2= [20, 3, 2]
# a = arr1 + arr2
# for i in range (0,len(a)):
#     for j in range (i,len(a)):
#         if (a[i]>a[j]):
#              x = a[i]
#              a[i]=a[j]
#              a[j]=x
# print(a)

# a = range(10)
# print(a)
# l = list(a)
# print(l)
# l1 = list(range(0,11,2))
# print(l1)


# for i in range(0,4):
#     for j in range (0,4):
#         print("#",end=" ")
#     print()

# n = int(input("Enter any number : "))
# for i in range(n,0,-1):
#     for j in range (i,0,-1):
#         print(i,end=" ")
#     print()

# import array as arr
# arr.a()

# from array import *
# val= array("i")#creating empty array for int
# n = int(input("Size of arr :"))
# for i in range(n):
#     x =int(input())
#     val.append(x)
# y = int(input("Search num :"))
# f = False
# for i in range(n):
#     if val[i]==y:
#         f = True
#         print(i)
#         break
# if f == False:
#     print("Not Found")

# name = ["Akshay","Samarth","Kunal","Mayur","Nishu"]
# lang = ["C++","Python","Java","C++",]   
# skills = dict(zip(name,lang))
# print(skills)
# skills["Samarth"]=["Python","Java"]
# print(skills)
# skills["Samarth"].append("JS")#adding in list of key
# print(skills)


# nums = [3,2,4]
# target =6
# d= {}
# for i in range (0,len(nums)):
#     d.update({nums[i]:i}) 
# print(d)
# for i in range(0,len(nums)):
#     x = target - nums[i]
#     if x in d and d[x]!=i:
#         print (i,d[x])
#         break

# x = int(input("enter any num"))
# y = str(x)
# z = y[::-1]
# print(y)
# print(z)


# s="MCMXCIV"
# l=list(s)
# print(l)
# l1 = []
# for i in range (0,len(l)):
#     if l[i]=="I":
#         l1.append(1)
#     elif l[i]=="V":
#         l1.append(5)
#     elif l[i]=="X":
#         l1.append(10)
#     elif l[i]=="L":
#         l1.append(50)
#     elif l[i]=="C":
#         l1.append(100)
#     elif l[i]=="D":
#         l1.append(500)
#     elif l[i]=="M":
#         l1.append(1000)
# print(l1[-1])
# sum = l1[-1]
# for i in range(0,len(l1)-1):
#     if l1[i]>l1[i+1]:
#         sum += l1[i]
#     else :
#         sum -=l1[i]
#     print(sum)

# l= []
# n = int(input("Enter :"))

# for i in range(0,n):
#     s=str(input())
#     l.append(s)
# s1 = ""
# d={}
# count = list(range(1,n+1))
# for i in range(0,n):
#     for j in range(0,len(l[i])):
#         if l[i][j] in d:
#             d.update({l[i][j]:count[i]})
#         else : d.update({l[i][j]:count[0]})
# print (d)

# nums = [0,0,1,1,1,2,2,3,3,4]
# i,j = 0,1
# k = 0
# while j<len(nums):
#     if nums[j]!=nums[i]:
#         k+=1
#         i+=1
#         nums[i] = nums[j]
#     j+=1  

# print(nums[0:k+1])


# x = "111100"
# y = "101" # it should be "000101"
# s=[]
# if len(y)<len(x):

# x= "1111"
# y = "1"
# diff = len(x) - len(y)
# y = "0"*diff + y
# print(y)
# strs = ["aaa","aa","aaa"]
# strs.sort()
# print(strs)
# ans=strs[0]
# print(ans[:-1])
# for i in strs[1:]:
#     while not i.startswith(ans):
#         ans = ans [:-1]
#         print(ans)
#         if not ans:
#             ans=""

# inter = [[1,3],[2,6],[8,10],[15,18]]
# inter.sort()
# i = 0
# while i < len(inter)-1:
#     if inter[i][1]>=inter[i+1][0]:
#         inter[i][1] = inter [i+1][1]
#         inter.pop(i+1)
#     i+=1
    

# print(inter)

s="geeksforgeeks"

m = Counter(s)
print(m)
for x in m:
    if m[x]>1:
        print(x,m[x])
        

# n = len(s)
# s = "".join(sorted(s))
# count = 1
# i = 0
# j = i+1
# l = []
# while j < n:
#     if s[i]==s[j]:
#         j+=1
#         count += 1
#     else :
#         if count > 1 :
#             l.append((s[i],count))
#             print(l)
#             l.pop()
#         i = j
#         j = i+1
#         count = 1
# if count > 1:
#     l.append((s[i],count))
#     print (l)