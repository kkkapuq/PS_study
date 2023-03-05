'''
문제 : 효율적인 해킹
난이도 : 실버 1
링크 : https://www.acmicpc.net/problem/1325
'''
'''
1. A가 B를 신뢰상태일 경우, B를 해킹하면 A도 해킹 가능하다.
2. 신뢰 관계가 주어졌을 때, '한번에' 가장 많은 해킹이 가능한 컴퓨터의 '번호' 출력

1) dfs로 돌면서, depth가 가장 깊은 컴퓨터의 번호를 list에 저장한다, 그리고 오름차순으로 출력하기
2) dfs로 안되는애인듯 ㅠㅠ bfs 시도해보기
'''
import sys
from collections import deque

n, m = map(int, input().split())
graph=[[] for _ in range(n+1)]
visited=[False] * (n+1)

for _ in range(1, m+1):
    a, b = map(int, sys.stdin.readline().split())
    # a->b 라면 이렇게 표현해야됨
    graph[b].append(a)
    
maxCnt = 0
answer = []

# def dfs(v, depth):
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i, depth+1)
#             visited[i] = True
#         # depth 비교
#         if maxDepth < depth:
#             maxDepth = depth
#             answer.append(v)

def bfs(v):
    visited = [False] * (n+1)
    visited[v] = True
    cnt = 1
    q = deque([v])
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt
    
for i in range(1, n+1):
    temp = bfs(i)
    if temp > maxCnt:
        answer = [i]
        maxCnt = temp
    elif temp == maxCnt:
        answer.append(i)
    
answer.sort()
print(' '.join(map(str, answer)))
