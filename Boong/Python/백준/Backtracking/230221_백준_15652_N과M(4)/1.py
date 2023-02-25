'''
문제 : N과 M(4)
난이도 : 실버 3
링크 : https://www.acmicpc.net/problem/15652
'''
'''
1. N과 M(2)에서 했던 조건을 걸어주면 끝아닌가?
2. 밑에 백트 도는 for문에서 v부터 시작해줘야 recursion 에러가 안걸린다.
'''
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
# 5, 2로 예를들자
s = []
cnt = 0

def dfs(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        global cnt
        cnt += 1
        return
    for i in range(v, n+1):
        # i = 1
            s.append(i)
            dfs(i)
            s.pop()
dfs(1)
print(cnt)