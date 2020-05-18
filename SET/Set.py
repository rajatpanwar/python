///A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

set = {"apple", "banana", "cherry"}
print(set)


<--------example2----------->
Days={"Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"}
print(Days)
print(type(Days))
print("------through looping print the days-----------")
for i in Days:
    print(i)
    
 <-------we can write 2nd example like this------->
Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])  
print(Days)  
print(type(Days))  
print("looping through the set elements ... ")  
for i in Days:  
    print(i)  
    
