'''
문제 : 크기가 작은 부분문자열
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/147355
'''
'''
1. 리스트 슬라이싱 하면 될거같은데?
'''

def solution(t, p):
    answer = 0
    
    t = list(t)
    n = len(t)
    m = len(p)
    
    for i in range(n-m+1):
        temp = ''.join(t[i:i+m])
        if int(temp) <= int(p):
            answer += 1
    
    return answer