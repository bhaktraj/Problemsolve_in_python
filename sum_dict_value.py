#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
l1 =  list(student_marks[query_name])
av_score = 0
for i in range(0,len(l1)):
    av_score = av_score+l1[i]

av_score = av_score/3
print("{:.2f}".format(av_score))
    