n = int(input())                        //take input from users

student_marks = {}                 //make a array

for _ in range(n):
    name, *line = input().split()          //The split() method splits a string into a list
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

print("{0:.2f}".format(round(sum(student_marks[query_name]) / len(student_marks[query_name]), 2)))
