import heapq
import sys


n = int(input())
workList = [list(map(int, input().split())) for _ in range(n)]
startTime = 99999999

workList.sort(key=lambda x:x[1])

for i in range(len(workList)):
    time = workList[i][0]
    for j in range(i):
        time += workList[j][0]
    if workList[i][1] < time:
        print(-1)
        break
    else:
        startTime = min(startTime, workList[i][1] - time)

print(startTime)