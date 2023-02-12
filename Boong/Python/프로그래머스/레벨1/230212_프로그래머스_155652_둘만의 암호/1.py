def solution(s, skip, index):
    answer = []
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z']
    skipList = []
    for i in skip:
        skipList.append(i)
        
    for i in range(len(s)):
        # 현재 위치
        cur = alphabet.index(s[i])
        tempNum = cur + index
        # index개만큼 뒤에 있는걸 뽑아줘야 되는데, 이 때 skipList에 있으면 걔네를 무시하고 다음껄 count 해줘야함
        while True:
            for j in range(1, index+1):
                temp = cur + j
                if temp > 25:
                    temp %= 26
                if alphabet[temp] in skipList:
                    tempNum += 1
            if tempNum > 25:
                tempNum %= 26
            if alphabet[tempNum] not in skipList:
                break
            
        answer.append(alphabet[tempNum])
                    
    
    return ''.join(answer)

print(solution('asdf', 'bcdetu', 5))