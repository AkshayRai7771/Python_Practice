#creating empty list
l=[]
print(l)
#adding multiple elements  
l.extend([12,88,1,76,32,67])
print(len(l))
print(l)

#adding one element
l.append(7)
print(l)
#adding one element at given index
l.insert(2,14)
print(l)
#removing min element 
l.remove(min(l))
print(l)
#removing element at particular index 
l.pop()
print(l)
#removing multiple
del l[5:]
print(l)
#sum 
print(sum(l))
#sort
l.sort()
print(l)
#using append in two list
l1=[1,3,6,2,9]
l2=[2,9,7,5,11]
l1.append(l2)
l1.extend(l2)
print(l1[::-1])
