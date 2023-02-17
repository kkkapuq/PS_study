'''
문제 : DFS와 BFS
난이도 : 실버 2
링크 : https://www.acmicpc.net/problem/1260
'''

from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
def bfs(v):
    visited = [False] * (n+1)
    q = deque([v])
    # 방문처리
    visited[v] = True
    while q:
        temp = q.popleft()
        print(temp, end=' ')
        for i in graph[temp]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
        

for i in range(1, m+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()
    
dfs(v)
print()
bfs(v)
    