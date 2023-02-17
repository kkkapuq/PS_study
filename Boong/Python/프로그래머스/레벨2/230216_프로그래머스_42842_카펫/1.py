'''
문제 : 카펫
난이도 : 레벨 2
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''

'''
1. 가로를 늘려보고 시행
2. 안되면 세로도 늘려보기
'''
### 틀린 풀이
'''

def solution(brown, yellow):
    # 행과 열은 최소 3x3 임
    r, c = 3, 3
    
    while True:
        tempBrown = brown
        tempYellow = yellow
        for i in range(r):
            for j in range(c):
                # 첫줄과 마지막줄은 무조건 갈색
                if i == 0 or i == r-1:
                    tempBrown -= 1
                # 사잇줄의 처음과 마지막은 갈색    
                elif (i > 0 and i < r-1) and (j == 0 or j == c-1):
                    tempBrown -= 1
                # 중앙은 노랑으로 채운다
                else:
                    tempYellow -= 1
        
        # 이 과정을 다 겪고나서 tempBrown과 tempYellow가 0이면 정답
        if tempBrown == 0 and tempYellow == 0:
            return [r, c]
        elif r == c:
            r += 1
        else:
            c += 1
'''

'''
1. 가로를 a, 세로를 b라고 둬보자.
2. yellow의 갯수는 (a-2)*(b-2)
3. brown = 2a + 2b - 4 (모서리 4개)
4. ab = total
5. a = total / b
'''

def solution(brown, yellow):
    # 행과 열은 최소 3x3 임
    a, b = 3, 3
    total = brown + yellow
    for b in range(1, total+1):
        a = total / b
        # 가로는 세로보다 같거나 길다
        if a >= b:
            if 2*a + 2*b - 4 == brown:
                return [a,b]
        