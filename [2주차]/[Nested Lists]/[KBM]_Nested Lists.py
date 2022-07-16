if __name__ == '__main__':
    stu_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        stu_list += [[name,score]]
        score_list += [score]
    
    second_lowest =sorted(list(set(score_list)))[1] # set() : 중복제거, list() : 다시 리스트 형태로 변환

    for a,b in sorted(stu_list):   # a = name, b = score
        if b == second_lowest :    # score 가 second_lowest 와 같을때
            print(a)               # name 출력
