/// A function can be defined as the organized block of reusable code which can be called whenever required. Python allows us to divide a large program into the basic building blocks known as function. The function contains the set of programming statements enclosed by {}.

<----------------------ADVANTAGE----------------------------->
AVOID REWRITING
REUSABLITY
WE CAN TRACK A LARGE PYTHON PROGRAM EASILY WHEN IT IS DEVIDED INTO MULTIPLE FUNCTION

<-------------------------SYNTAX-------------------------------------->
In python, we can use def keyword to define the function.

def my_function():  
    function-suite   
    return <expression>  
  
<---------------------------example1------------------------------------>
def function():
  print("hello world")
function()  


<-------------------------example2-------------------------------------->
a=int(input("enter first number"))
b=int(input("enter second number"))

def add():
    c=a+b;
    print(c)
 add()   
    
 <-------------------example3----------------------------------------->
//pass the paramenter in the function

def function(Name):
    print("Hi",Name)
function("Rajat")

<-----------------example4------------------------------->

a=int(input("enter the first no "))
b=int(input("enter the second no"))
def sub(x,y):
    c=a-b;
    return c;
print("substraction is ",sub(a,b))   

<------------------example5------------------------>
//print the list through a function

def fun_list(list1):
    list1.append(40)
    list1.append(5)
    print(list1)
    
list1=[10,20,30]

fun_list(list1);     //function calling 
                           //till here function  print the list
print("list is :",list1)   //outside the function again rint the list
    
    
       
    
  

