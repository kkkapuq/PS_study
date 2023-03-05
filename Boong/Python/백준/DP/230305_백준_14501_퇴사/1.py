'''
문제 : 퇴사
난이도 : 실버 3
링크 : https://www.acmicpc.net/problem/14501
'''
'''
1. 1일부터 시작
2. 상담기간이 N을 초과하면 그 일자의 상담은 불가능함
3. 돈을 많이 벌 때의 금액을 구하자

1) DP문제인거같으니까 그냥 최대 수익만 업데이트 해주면 되지않을까?
2) 점화식...은...
'''

n = int(input())
consult = []
dp = [0 for _ in range(n+1)]

# 상담 일수와 수익 저장
for i in range(n):
    t, p = map(int, input().split())
    consult.append([t, p])
    
# # 상담을 할떄랑 안할 때 모두 탐색
# for i in range(n):
#     if i + consult[i][0] <= n:
#         # i번째 날에 상담을 하는 경우   
#         dp[i+consult[i][0]] = max(dp[i+consult[i][0]], dp[i]+consult[i][1])
#     # 상담을 하지 않는다면 재설정
#     dp[i+1] = max(dp[i+1], dp[i])

for i in range(n-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
    if i+consult[i][0] > n:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하는것과 상담을 안하는 것 중 더 큰 것을 선택
        dp[i] = max(dp[i+1],consult[i][1] + dp[i+consult[i][0]])
        
print(dp[0])
# print(dp[-1])
            