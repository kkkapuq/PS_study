'''
문제 : 가장 가까운 같은 글자
난이도 : 레벨 0
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/142086
'''
'''
1. 딕셔너리에 현재 인덱스의 위치를 넣어준다. dict[b] = 0 이런식으로
2. 만약 dict[b]가 존재하지 않는다면 dict[b] = 현재인덱스 로 넣어주고, 존재한다면 해당 인덱스와 현재 인덱스의 거리를 구하고, 현재 인덱스로 업데이트 해준다.
3. 거리를 구할 때 거리를 answerList 에 append 해주자
'''


def solution(s):
    answer = []
    wordDict = {}
    
    for index, i in enumerate(s):
        if i not in wordDict:
            wordDict[i] = index
            answer.append(-1)
        else:
            answer.append(abs(index - wordDict[i]))
            wordDict[i] = index
    
    return answer

solution('banana')