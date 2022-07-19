if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()) #map: 리스트의 요소를 지정된 함수로 처리해주는 함수 / 이 줄의 결과는 문자열 리스트
    
    integer_list = tuple((integer_list)) #tuple: 리스트를 튜플로 변환하는 함수
    
    print(hash(integer_list)) #hash: 숫자가 아닌 다른 값(문자열, 튜플)을 인덱스로 사용할 때 쓰는 함수, 이름을 넣으면 그에 따른 고유값이 나옴
