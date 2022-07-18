if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    title = list(student_marks[query_name])    
    percent = sum(a)/3;
    print("%.2f" % percent);  
