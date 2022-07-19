records = []
n = int(input())
for _ in range(n):
    name = input()
    score = float(input())
    records.append([name,score])
records_sor = sorted(records)
want = records_sor[1][1]   
for name, score in records_sor :
  if score == want :
    print(name)
    
# records = [[name1,score1],[name2,score2],,,[name_n,score_n]]형식으로 정리
# want는 정렬이 완성되었을 때 리스트 2번째 위치의 2번째 값 = 2번째로 점수가 낮은 사람(2번째 위치)의 점수(2번째 값)
# 9번째 줄은 score가 같은 사람이 여러명 있을 수 있으므로 want값과 score가 같은 사람을 모두 찾아서 출력.
# 알파벳 순서는 records_sor를 통해 정렬되었으므로 고려하지 않아도 된다.
