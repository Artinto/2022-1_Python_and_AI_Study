def mutate_string(string, position, character):
    a=string[:position]+character+string[position+1:]#정해진 포지션 사이에 넣어야 하는 값을 넣을 수 있도록 :pos, pos+1:을 이용
