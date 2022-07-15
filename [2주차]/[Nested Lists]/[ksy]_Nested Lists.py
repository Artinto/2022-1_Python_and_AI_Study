if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    student=sorted(student,key=lambda x:x[1])#score을 기준
    second_lowest_score=sorted(list(set([x[1] for x in student])))[1]#두번쨰로 제일 작은값
    a=[]
    for i in student:
        if i[1]== second_lowest_score:
            a.append(i[0])#이름 넣기
    a.sort()
    for i in a:
        print(i)
