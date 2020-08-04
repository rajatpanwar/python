from datetime import date
import calendar
T=int(input())
for x in range(T):
   
    t1=list(map(str,input().split(" ")))
    t2=list(map(str,input().split(" ")))
    hrs=int(''.join(list(t1[4])[0:2]))-(int(''.join(list(t2[4])[0:2])))
    mins=int(''.join(list(t1[4])[3:5]))-(int(''.join(list(t2[4])[3:5])))
    secs=int(''.join(list(t1[4])[6:]))-(int(''.join(list(t2[4])[6:])))
    hrtz1=int(''.join(list(t1[5])[1:3]))
    hrtz2=int(''.join(list(t2[5])[1:3]))
    mintz1=int(''.join(list(t1[5])[3:]))
    mintz2=int(''.join(list(t2[5])[3:]))
    month1=t1[2]
    month2=t2[2]
    d0=date(int(t1[3]),list(calendar.month_abbr).index(month1),int(t1[1]))
    d1=date(int(t2[3]),list(calendar.month_abbr).index(month2),int(t2[1]))
    delta=d0-d1
    dayz=delta.days
    if(str(list(t1[5])[0])== "-"):
        hrs=hrs+hrtz1
        mins=mins+mintz1
        
    if(str(list(t1[5])[0])== "+"):
        hrs=hrs-hrtz1
        mins=mins-mintz1
        
    if(str(list(t2[5])[0])=="-"):
        hrs=hrs-hrtz2    
        mins=mins-mintz2
        
    if(str(list(t2[5])[0])=="+"):
        hrs=hrs+hrtz2
        mins=mins+mintz2

    difference=dayz*86400 + hrs*3600 + mins*60+secs
    print(abs(difference))
