def mutate_string(string, position, character):    //create a function
    list2=list(string)
    list2[position]=character      
    return ''.join(list2)

  
if __name__ == '__main__':     //main functiom
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
