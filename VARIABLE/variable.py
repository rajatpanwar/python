x,y,z= "rajat","rithik","nipun"
print(x)
print(y)
print(z)         //output is rajat , rithik ,nipun




<-----2nd example---->

x = y = z = "Rajat"
print(x)
print(y)
print(z)     //output is -- Rajat,Rajat, Rajat



<---3rd example--->
 
 --add two string--
x = "awesome"
print("Python is " + x)    //output is -- python is awesome

<---4th example--->

//we can write 3rd example with the help of this 3rd variable
x="Awesome"
y="python is"
z=(y+x)
print(z)        //output is--- python is awesome



<----GLOBAL VARIABLE---->

variable that are created outside the function called gloabal variable

x="Awesome"
  def fun()                //def keyword is used in python to define the function and we can write def before the function name
 print("python is "+x)
 fun()                   //output is --pyton is Awesome
