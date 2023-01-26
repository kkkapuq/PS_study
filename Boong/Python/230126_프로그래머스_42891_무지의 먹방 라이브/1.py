'''
1. 1번부터 번호가 증가하는 순서대로 음식이 온다.
2. 마지막을 먹으면 다시 1번으로
3. 음식 하나를 1초동안 먹는데, 남은건 두고 다음음식을 먹음
4. k 번째 먹은 음식의 다음꺼를 구하면 됨.
'''
'''
### 아이디어 ###
1. while은 써야될거같은데... 시초는 무조건 나니까 반복 수를 줄여야 함
2. n번째 음식을 다 먹기위해 걸리는 시간은 n * 남은 음식의 개수
3. 따라서 k를 줄이려면... 시간이 작은 음식을 먼저 처리하면 자연스럽게 while문은 축소가 된다.
4. 힙큐?
'''
import heapq

def solution(food_times, k):
    answer = -1
    
    # 방송 중단 전에 음식을 다 먹으면
    if sum(food_times) <= k:
        return answer
    
    foodList = []
    # 우선순위 큐에 음식 번호랑 음식 넣기
    for index, i in enumerate(food_times):
        heapq.heappush(foodList, (i, index+1))
    
    # 남아있는 음식의 길이
    l = len(foodList)
    # 음식을 먹는데 드는 총 시간
    time = 0

    # 현재 음식을 먹기 위해 필요한 시간((현재음식 시간 - 이전음식 시간) * 남은음식갯수) > k 면 반복문 종료
    while (foodList[0][0] - time) * l < k:
        # k까지 도달하는 시간을 빼주기
        k -= (foodList[0][0] - time) * l
        # time에 총 시간 더해주기
        time += (foodList[0][0] - time)
        # 음식 길이 하나 줄여주기
        l -= 1
        # pop 해주기
        heapq.heappop(foodList)
    
    # 음식 번호 기준으로 재정렬
    sortedList = sorted(foodList, key = lambda x : x[1])
    # 줄어든 k를 기준으로, k % l 번째 음식이 정답...
    answer = sortedList[k % l][1]
    return answer


print(solution([3, 1, 2], 5))