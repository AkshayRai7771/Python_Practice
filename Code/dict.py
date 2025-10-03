d = {}
d.update({"Name":"Akshay","Roll No.":1,"Age":25})
k = d.copy()#deep copy if k= d then it will be shallow 
d.update({"Name":"Samarth"})
print(d)
print(k)
print(d.keys())
print(d.values())
d.pop("Age")
print(d)
print(d.get(25,"Not Found"))
print(d["Name"])
# print(d["Place"]) keyerror bcz no key found 

name = ["Akshay","Samarth","Kunal","Mayur","Nishu"]
lang = ["C++","Python","Java","C++",]   
skills = dict(zip(name,lang))
print(skills)     
skills["Mayank"]= "ReactJS"
print(skills)
del skills["Akshay"]
print(skills)