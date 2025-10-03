#set is a collection of uniques elements ,can be int , float or any other data type
#creating empty set
s = set()
#adding multiple elements
s.update({1,22,67,11,12,1,2,2,2,(90,76,66),"d"})
print(s)
#adding element 
s.add(7)
print(s)
#removing element 
s.remove(1)
print(s)
#removing unknown without any error 
s.discard(11)
print(s)
#removing from index is not possible as set is unordered 
s.pop()
print(s)
#union is two sets 
s1={1,2,3,"m","m","e",2}
s2={4,3,2,"r","y"}
print(s1.union(s2))
#intersection 
print(s1.intersection(s2))