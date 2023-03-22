'''
문제 : 단지번호 붙이기
난이도 : 실버 1
링크 : https://www.acmicpc.net/problem/2667
'''

from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#단지의 세대 수
nums = []
count = 0

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

def bfs(x, y):
    global graph
    n = len(graph)
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    count = 1
    
    while q:
        # 큐에 들어있는 친구 하나 뽑고 상하좌우 체크
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 만약 주변에 집이 있으면, 큐에 해당 좌표를 늘려주고 현재 집은 0으로 미방문되도록 설정
            # count += 1 해줘서 단지 내 집 개수 추가
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    return count


for i in range(n):
    for j in range(n):
        # 모임인 집이 존재한다면
        # dfs 풀이
        '''
        if dfs(i, j) == True:
            nums.append(count)
            count = 0
        '''
        # bfs 풀이
        if graph(i, j) == 1:
            nums.append(bfs(i, j))
        

nums.sort()
print(len(nums))
for i in nums:
    print(i)