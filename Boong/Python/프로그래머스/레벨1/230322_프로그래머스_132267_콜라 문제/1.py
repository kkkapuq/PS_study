'''
문제 : 콜라 문제
난이도 : 레벨 1
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/132267
'''
'''
1. a개를 주면 b로 받는다, n은 (n // a) + (n % a)가 되고, b를 일단 갖고있는다.
2. 개수가 맞아떨어지지 않는 빈병은 가지고있다가 나중에 써먹을 수 있다.
'''
'''
# 틀린 풀이
import sys
sys.setrecursionlimit(10000)

answer = 0

def solution(a, b, n):
    global answer
    if n < 2:
        return answer + n
    # 마트에서 교환가능한 개수 + 교환하고 남는 개수
    n = ((n//a)*b) + (n%a)
    answer += n
    solution(a, b, n)
    
    return answer

'''
def solution(a, b, n):
    answer = 0
    # 빈 병을 교환하고 남은 빈 병
    keep = 0
    while n >= 2:
        # n = 마트에서 교환해서 갖고있는 빈 병의 수
        if n % a > 0:
            keep += (n%a)
        n = ((n//a)*b)
        answer += n
        if n < a and n + keep >= a:
            n = (((n+keep)//a)*b)
            keep -= (n+keep)//a
            answer += n
        elif n < a and n + keep < a:
            answer += n + keep
    
    return answer

solution(3, 1, 20)