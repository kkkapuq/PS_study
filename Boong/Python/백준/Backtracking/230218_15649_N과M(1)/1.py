'''
문제 : N과M (1)
난이도 : 실버 3
링크 : https://www.acmicpc.net/problem/15649
'''

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

def dfs():
    # 만약 s의 길이가 m과 같다면 출력하고 continue
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    else:
        # 1부터 n까지 탐색하기
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                s.append(i)
                dfs()
                # m개의 숫자를 다 체크하고 난 뒤에 다음 수가 들어올 자리를 만들어줘야됨
                s.pop()
                # 해당 자리는 방문하지 않은 걸로 하기
                visited[i] = False

dfs()