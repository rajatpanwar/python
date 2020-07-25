// Till now, we were taking the input from the console and writing it back to the console to interact with the user.

//Sometimes, it is not enough to only display the data on the console. The data to be displayed may be very large, and only a limited amount of data can be displayed on the console, and since the memory is volatile, it is impossible to recover the programmatically generated data again and again.

//However, if we need to do so, we may store it onto the local file system which is volatile and can be accessed every time. Here, comes the need of file handling.



file object = open(<file-name>, <access-mode>, <buffering>)  //the syntax to use the open() function is

<----------------example1----------------------->

fileptr=open("file.txt","r")          //open the file
if fileptr:
  print("file open successsfully")
  fileptr.close()                          //close the opened file
                                            //here is close function no attribute so the program will show the error 
                                           //this is the only use that how to use the function
      
 <---------------example2 (how to write in a file)------------------------>

fileptr=open("file.txt","w")
fileptr.write("python is a modern modern day language it makes thing so simple")
fileptr.close()

<----------------example3(how to read froma file)--------------------->
fileptr=open("read.txt","r")
content=fileptr.readlines()
print(content)
fileptr.close()


<--------------------example4(read from the file through for loop)--------------------------->

fileptr=open("read1.txt","r")
for i in fileptr:
  print(i)



      
      
             
