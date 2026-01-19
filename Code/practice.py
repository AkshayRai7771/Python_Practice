from collections import Counter
from functools import reduce
from datetime import datetime,timedelta,date
import array
from itertools import permutations
from collections import Counter
from math import gcd
import requests
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

# s="geeksforgeeks"

# m = Counter(s)
# print(m)
# for x in m:
#     if m[x]>1:
#         print(x,m[x])
        

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

# def fact(num):
#     if num == 1:
#         return 1
#     total = num*fact(num-1)
#     return total

# n = int(input("Enter any Number : " ))
# factorial = fact(n)
# print(factorial)


#Map,reduce,filter using lambda(unnamed func)
# n = int(input("Enter any number : "))
# l = []
# for i in range(0,n**2):
#     l.append(i)

# odd= list(filter(lambda x : x%2 != 0,l))
# print(odd)

# odd_to_even = list(map(lambda x : x*2 , odd))
# print(odd_to_even)

# even_to_one = list(map(lambda x : x - x +1,odd_to_even))
# print(even_to_one)

# length = reduce(lambda x,y : x+y , even_to_one)
# print(length)
# s = 'ABCDCDC'
# ss = 'CDC'

# x =s.count(ss)
# print(x)
# count = 0
# n = len(s)
# m = len(ss)
# print(s[0:m])
# for i in range (0,n-m+1):
#     if s[i] == ss[0]:
#         if s[i:i+m] == ss:
#             print(s[i:i+m])
#             count+=1
# string = 'BANANA'
# v ='AEIOU'
# s = {}
# k = {}
# for i in range(0,len(string)):

#     for j in range(i,len(string)):
#         if string[i] in v:
#             k.update({string[i:j+1]:string.count(string[i:j+1])})
#         else :
#             s.update({string[i:j+1]:string.count(string[i:j+1])})

# print(s)
# print(k)
# y = z.strftime("%d-%m-%Y")
# x = datetime.now() - timedelta(days= 30)
# y = datetime.now().strftime("%d-%m-%Y")

# date_str = "10-08-2025"
# date_obj = datetime.strptime(date_str, "%d-%m-%Y").date()
# print(date_obj)

# formatted_string = date_obj.strftime("")

# print(formatted_string)   # 08 October, 2025 10:45 PM (string)

# print(y)

# arr = array.array('i',[1, 3, 5, 5, 5, 5, 67, 123, 125])
# l = []
# x = 5
# i = arr.index(x)
# print(i)

# s , n = input().split()
# ss = sorted(s)
# print(list(permutations(ss,int(n))))
# count = 0
# for i in permutations(ss,int(n)):
#     count+=1
#     print("".join(i))
# print(count)
# arr = array.array("i",[4, 3, 6, 2, 1, 1])
# d = {}
# l = []

# for i in range(0,len(arr)):
#     d[i+1] = 0
# for i in range(0,len(arr)):
#     if arr[i] in d:
#         if d[arr[i]] == 1:
#             l.append(arr[i])
#         d[arr[i]]+=1

# for x in d:
#     if d[x]==0:
#         l.append(x)
# if len(arr)==1:
#     ans = arr[0]
# else:
#     mp = Counter(arr)
#     for x in mp:
#         if mp[x]>1:
#             ans = x 

# print(mp)

# print(l)

#s,n = input().split()
#ss = sorted(s)

#for i in permutations(ss,int(n)):
  #  print("".join(i))#


# print(len(l))

# l = [90, 70, 20, 80, 50]
# l.sort()
# x = 90
# bool = False
# if len(l)<=1 or l[-1]-l[0]<x:
#     bool = False


# print(bool,l[-1])

# arr = [1,2,3,4]
# arr = arr[::-1]
# print(arr)

# N=4
# Mat=[[10,20,30,40],
# [15,25,35,45],
# [27,29,37,48],
# [32,33,39,50]]

# l = []
# for row in Mat:
#     for x in row:
#         l.append(x)
# l.sort()
# print(l)


# no_of_test = int(input())
# l = []
# for i in range(0,no_of_test):
#   x,y = map(int,input().split())
#   l.append(x)
#   l.append(y)

# num = 1
# den = 1
# for i in range(0,len(l)):
#   if i % 2 != 0 :
#     den = den * l[i]
#   else:
#     num = num * l[i]
    
    

# g = gcd(num,den)

# num = num // g
# den = den // g

# print(num,end=" ")
# print(den)


# def score_words(words):
#   score = 0
#   for word in words:
#       num_vowels = 0
#       for letter in word:
#           if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
#               num_vowels += 1
#           print(num_vowels,"Vowels")
#       if num_vowels % 2 == 0:
#           score += 2
#       else:
#           score+=1
#       print(score)
#   return score


# n = int(input())
# words = input().split()
# print(score_words(words))

#Email Validation
# def fun(s):
#     try:
#         username , rest = s.split("@")
#         website , extension = rest.split(".")
#     except ValueError:
#         return False
    
#     if not (extension.isalpha() and len(extension)<=3):
#         return False
    
#     if not website.isalnum():
#         return False
#     allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
#     for ch in username:
#         if ch not in allowed:
#             return False
    
#     return s  
    
# def filter_mail(emails):
#     return list(filter(fun, emails))

# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())

# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)

#BINARY SEARCH
# a = [10,9,7,6,5,4,2,1]
# a = [1,2,4,5,6,7,9,10]
# m = 2 
# left = 0
# right = len(a)-1
# res = -1
# while left <= right:
#     mid = int((left+right)/2)
#     if a[left]>a[right]:
#       if a[mid] == m:
#           res = mid
#           print("Yes list is desc")
#           break
#       elif a[mid]<m:
#           right = mid-1
#       else :
#           left= mid+1
#     else:
#         if a[mid] == m:
#           res = mid
#           print("Yes list is asec")
#           break
#         elif a[mid]>m:
#             right = mid-1
#         else :
#             left= mid+1
# print(res)

# First and last occurance 

# a = [1,2,3,3,3,3,3,6,7,8,9]
# m = 3


# first = -1
# last = -1

# for i in range(0,2):
#     left = 0
#     right = len(a)-1
#     if first == -1:
#       while left <=right:
#           mid = int((left+right)/2)
#           if a[mid]==m:
#               first = mid
#               right = mid-1
#           elif a[mid]>m:
#               right = mid -1
#           else :
#               left = mid+1
#     elif last == -1:
#       while left <= right:
#           mid = int((left+right)/2)
#           if a[mid]==m:
#               last = mid
#               left = mid+1
#           elif a[mid]>m:
#               right = mid -1
#           else :
#               left = mid+1
# print(first,last)

#No of rotations

# a = [4,5,6,7,0,1,2]
# left = 0
# right = len(a)-1
# n = len(a)
# while left<=right:
#     mid = (left+right)//2
#     next = (mid +1) % n
#     pre = (mid + n -1) % n
#     if a[mid]<=a[next] and a[mid]<=a[pre]:
#         if a[mid]==a[next] and a[mid]==a[pre]:
#             print(left)
#         else:
#             print(mid)
#         break
#     if a[left]<=a[mid]:
#         left = mid 
#     elif a[mid]<= a[right]:
#         right = mid 

# nums1 = [1,2]
# nums2 = [2,4]
# big = []
# left = 0
# right = 0
# while left < len(nums1) and right<len(nums2):
#     if nums1[left]<= nums2[right]:
#         big.append(nums1[left])
#         left+=1
#     else:
#         big.append(nums2[right])
#         right+=1

# while left < len(nums1):
#     big.append(nums1[left])
#     left += 1

# while right < len(nums2):
#     big.append(nums2[right])
#     right += 1
# print(big)

#Nearly Sorted list
# a = [70,80,90,100,40,50,60]
# target = 40
# left = 0 
# right = len(a)-1
# ans = -1

# while left <= right:
#     mid = ((left+right)//2)
#     if a[mid] == target:
#         ans = mid
#         break
#     elif left>=0 and a[mid-1]==target:
#         ans = mid-1
#         break
#     elif right<=len(a)-1 and a[mid+1]==target:
#         ans = mid+1
#         break
#     print(mid)
#     if a[left]<a[mid-1]:
#         right = mid-2
#     else:
#         left = mid+2
# print(ans)

# import requests
# category_count = input().lower()
# page =1 
# min_price = int(input())
# mx_price = int(input())
# total = 0
# while True:

#     url = f"https://jsonmock.hackerrank.com/api/inventory?page={page}"
#     response = requests.get(url)
#     result = response.json()

#     inventory_data = result["data"]
    

#     for single_inv in inventory_data:
#         category_name = single_inv["category"].lower()
#         ava_item = single_inv["available"]
#         item_price = single_inv["price"]
#         if min_price<=item_price <=mx_price and category_name==category_count:
#             total+=1
        
        
#     if page >= result["total_pages"]:
#         break
    
#     page += 1
    


# print(total)


# max sum of subarray of size k
a = [1,2,3,4,5,6,7,8,9]
x = 3
i = 1
j = x
# sums = 0
# while j<=len(a):
#     sums = max(sums,sum(a[i:j]))
#     i+=1
#     j+=1
#     print(sums)
# print(sums)

list_of_sum = [sum(a[i-1:j])]
while j < len(a):
    sums = list_of_sum[i-1] - a[i-1]+a[j]
    list_of_sum.append(sums)
    i+=1
    j+=1

print(list_of_sum)
print(max(list_of_sum))
    

#1st negative no in window of size k
# a =[1,-2,3,-4,5,-6,7,8,9]
# k = 3
# i =0
# j = i+k

# while j<=len(a):
#     for x in a[i:j]:
#         if x < 0:
#             print(x)
#             break
#     else:
#         print(0)
#     i+=1
#     j+=1
              
        




        


