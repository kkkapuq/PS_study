def solution(s, skip, index):
    # answer = []
    
    # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    #            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    #            'w', 'x', 'y', 'z']
    # skipList = []
    # for i in skip:
    #     skipList.append(i)
        
    # for i in range(len(s)):
    #     # 현재 위치
    #     cur = alphabet.index(s[i])
    #     tempNum = cur + index
    #     # index개만큼 뒤에 있는걸 뽑아줘야 되는데, 이 때 skipList에 있으면 걔네를 무시하고 다음껄 count 해줘야함
    #     while True:
    #         # 현재위치에서 j만큼 범위를 탐색, skipList에 있다면 tempNum을 더해줘서 그만큼 더 탐색하게 함
    #         for j in range(1, index+1):
    #             temp = cur + j
    #             # 25보다 크다면 26의 나머지만큼의 alphabet[temp] 로 되도록.
    #             temp %= 26
    #             # 그렇게 해서 변환된 temp가 skipList에 있다면 
    #             if alphabet[temp] in skipList:
    #                 tempNum += 1
    #         if tempNum > 25:
    #             tempNum %= 26
    #         if alphabet[tempNum] not in skipList:
    #             break
            
    #     answer.append(alphabet[tempNum])
    # return ''.join(answer)
    
    answer = ''
    
    skip_dict = dict()
    for skip_case in skip:
        skip_dict[ord(skip_case)] = True
    
    for letter in s:
        letter_code = ord(letter)
        convert_count = 0
        while convert_count < index:
            letter_code += 1
            if letter_code > ord('z'):
                letter_code = ord('a')
            if skip_dict.get(letter_code):
                continue
            else:
                 convert_count += 1
        answer += chr(letter_code)
        
    return answer

print(solution('asdf', 'bcdetu', 5))