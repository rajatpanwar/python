def minion_game(string):
    sp,kp = 0,0
    l = len(string)
    for i in range(0,l):
        k=l-i
        if string[i] in "AEIOU":kp+=k;
        else: sp+=k
    if sp>kp:print("Stuart",sp)
    elif sp==kp :print("Draw") 
    else:print("Kevin",kp)

if __name__ == '__main__':
    s = input()
    minion_game(s)
