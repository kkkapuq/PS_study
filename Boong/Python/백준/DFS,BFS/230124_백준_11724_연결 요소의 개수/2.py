'''
1. graph[x] = y, graph[y] = x 로 두고 dfs/bfs 돌리기
2. 

'''
import sys
sys.setrecursionlimit(10000)
from collections import deque

n, m = map(int, input().split())

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
       
def bfs(v):
    visited[v] = True
    q = deque([v])
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

graph = [ [] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(1, n+1):
    if not visited[i] :
        bfs(i)
        cnt += 1

print(cnt)