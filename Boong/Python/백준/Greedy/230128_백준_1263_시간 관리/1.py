import heapq
import sys


n = int(input())
workList = [list(map(int, input().split())) for _ in range(n)]
startTime = 99999999

workList.sort(key=lambda x:x[1])

# i번째 마감시간 이전에 사용시간들을 모두 더해서 마감시간보다 크다면 -1 return 하고 프로그램 종료
# 아니라면 현재 마감시간에서 사용시간을 빼서 최소값에 저장
for i in range(len(workList)):
    time = workList[i][0]
    for j in range(i):
        time += workList[j][0]
    if workList[i][1] < time:
        print(-1)
        exit()
    else:
        startTime = min(startTime, workList[i][1] - time)

print(startTime)