import textwrap
from collections import OrderedDict
def merge_the_tools(string, k):                  //define function
    list2=[]
#devides string into n equal parts of size k
    list1 = textwrap.wrap(string, k)

    for i in list1:
#removes duplicate characters from string and append it to list 2
        list2.append("".join(OrderedDict.fromkeys(i)))

    for i in list2:
        print(i)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
