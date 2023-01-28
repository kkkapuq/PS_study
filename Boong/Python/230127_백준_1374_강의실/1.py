'''
1. 가장 많은 강의를 듣게 하려면 강의시간이 적은놈들을 최우선으로 처리해야함
2. 그다음 heapq를 돌면서 현재 강의실에 i번째 강의가 들어올 수 있는지 판별, 들어올 수 없다면 append로 강의실 개설해주기
3. 근데 이러면 2중 for문 돈다. 이건 아닌듯
'''

import heapq
import sys

n = int(input())
lectList = []

for i in range(n):
    lectList.append(list(map(int, sys.stdin.readline().split())))

# 시작시간 순으로 정렬
lectList.sort(key= lambda x:x[1])

# len(q)는 강의실 개수, 수업이 끝나는 시간을 저장한다.
q = []
count = 0
for i in lectList:
    while q and q[0] <= i[1]:   # i번째 수업의 시작시간이 사용중인 강의실의 종료시간 이후라면
        heapq.heappop(q)        # 이 강의실을 같이 쓸 수 있는거니까 pop을 해준다, 이 과정을 겪다보면 결국엔 1개의 강의실로 좁혀지게 된다.
                                # while문이 이해가 잘 안갔는데, 최소한의 강의실을 구하기 위한 로직이다.
    heapq.heappush(q, i[2])     # 그리고 해당 수업이 끝나는 시간을 push.
    count = max(count, len(q))  # for문이 끝날 때마다 count 갱신해주기.

print(count)