emp=["Rajat",21,500069414]
Dep1=["CSE",10]
Dep2=["ECE",15]
HOD_CS=["MONIT KAPPOR",20]
HOD_ECE=["PArteek jha",35]

print("<----print employee_detail---->")
print("Name %s,age %s,ID %d"%(emp[0],emp[1],emp[2]))
print("<---print Dep detail---->")
print("1.Department1:\nBranch : %s, \nId: %d \n 2.Department2 \nBranch: %s,\nId: %d"%(Dep1[0],Dep1[1],Dep2[0],Dep2[1]))
print("<---print HOD detail---->")
print("Name :%s \nid: %d"%(HOD_CS[0],HOD_CS[1]))
print("Name :%s \nid: %d"%(HOD_ECE[0],HOD_ECE[1]))

print(type(emp),type(Dep1),type(Dep2),type(HOD_CS),type(HOD_ECE));     // in python type keyword tell the type of datatype
