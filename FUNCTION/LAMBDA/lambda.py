//  the anonymous functions are declared by using lambda keyword. However, Lambda functions can accept any number of arguments, but they can return only one value in the form of expression.


<-----------example1--------------------->
x=lambda a:a+10;                       //a is an argument and a+10 is an expression which got evaluated and returned.
print("sum is",x(30))  //output is --  40

<------------------example2--------------------->
x=lambda a,b:a+b;       //paas two argumant in lambda function

print("sum is",x(20,50))   

<--------------example3--------------------->
n=int(input("enter a number"))
b=lambda a:a*n;
for i in range(1,11):
    print(n,"X",i,"=",b(i))
