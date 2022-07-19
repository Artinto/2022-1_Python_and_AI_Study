n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
score = list(student_marks[query_name])
average = (score[0]+score[1]+score[2])/3
print(f'{average:.2f}')

# 소숫점 n째자리까지 표현 하는 방법 : print(f'{변수명:.nf}')
