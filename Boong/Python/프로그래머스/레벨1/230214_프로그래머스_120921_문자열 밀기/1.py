'''
문제 : 문자열 밀기
난이도 : 레벨 0
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120921

1. 큐로 A 길이만큼 for문 돌다가 B와 같아지면 break 하고 cnt return
'''

from collections import deque

def solution(A, B):
    answer = 0
    n = len(A)
    q = deque(list(A))
    
    if A == B:
        return answer
    
    for i in range(n):
        q.appendleft(q[n-1])
        q.pop()
        answer += 1
        
        if ''.join(q) == B:
            return answer
        
        if i == n-1:
            return -1
            
            
    
    
    
    return answer