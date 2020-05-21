/// A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets

<--------example1------->
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

<-------example2--------->
// how to access the element in dictionary

detail= {
    "Name":"Rajat panwar",
    "sapid":500069414,
    "Roll no":80,
    "course":"B.Tech",
    
}
x=detail["Name"]
print(x)

<-----------example 3----- ------------>
//access the element

detail= {
    "Name":"Rajat panwar",
    "sapid":500069414,
    "Roll no":80,
    "course":"B.Tech",
    
}
print("Name :%s "%detail["Name"])
print("sapid :%d "%detail["sapid"])
print("Roll no :%d "%detail["Roll no"])
print("course :%s "%detail["course"])
