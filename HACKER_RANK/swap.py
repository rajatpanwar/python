//swap the function
def swap_case(s):    //define function
    a = ""
    for let in s:
        if let.isupper() == True:
            a+=(let.lower())
        else:
            a+=(let.upper())
    return a
