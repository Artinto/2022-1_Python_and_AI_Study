n = int(input())
student_marks = {}
result=0
for _ in range(n):
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name] = scores
  

query_name = input()

result = (sum(student_marks[query_name])/len(line))
  
print('%0.2f' %result)
