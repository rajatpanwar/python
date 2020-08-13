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

<------------example4------------------->
// add new data in the dictionary
detail= {
    "Name":"Rajat panwar",
    "sapid":500069414,
    "Roll no":80,
    "course":"B.Tech",
    
}
print(detail)
print("<------enter new detail---------->")
detail["Name"]=input("Name ")
detail["sapid"]=int(input("sapid "))
detail["Roll no"]=int(input("Roll no "))
detail["course"]=input("course ")
print("-----printing the new data-------")
print(detail)

<-------example5-------------->
//similiar to example3
detail= {
    "Name":"Rajat panwar",
    "sapid":500069414,
    "Roll no":80,
    "course":"B.Tech",
    
}
x=detail.get("Name")      //we can use get function to access the element 
print(x)

<-------example6------------>
//print all the attribute on by one using for loop
detail= {
    "Name":"Rajat panwar",
    "sapid":500069414,
    "Roll no":80,
    "course":"B.Tech",
    
}
for i in detail:
    print(i)       //output is --- Name,sapid,Rollno,course
    
  <-------------example7--------------------->
  //print all the value of key attribute
  detail= {
    "Name":"Rajat panwar",
    "sapid":500069414,
    "Roll no":80,
    "course":"B.Tech",
    
}
for i in detail:
    print(detail[i])
    
    //output is---  Rajat Panwar
                    500069414
                    80
                    B.Tech
 <------------example8------------------------>
detail= {
    "Name":"Rajat panwar",
    "sapid":500069414,
    "Roll no":80,
    "course":"B.Tech",
    
}
for i,j in detail.items():      //using items() function we can print  key and value both
    print(i,j)
  
  <-----------------------example9---------------->
  detail= {
    "Name":"Rajat panwar",
    "sapid":500069414,
    "Roll no":80,
    "course":"B.Tech",
    
}
del detail["sapid"]      // use del we can remove the key and value for the dctionary
print(detail)   
  
  
  
  
  

