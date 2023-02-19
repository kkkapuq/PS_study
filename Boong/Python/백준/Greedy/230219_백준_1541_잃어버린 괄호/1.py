'''
1. - 뒤에 붙는 애들을 싹 다 묶어버리면 그게 최소다
2. + 로 split 하고 sum(list) 해준걸 계속 -= 해주자
'''
'''
# 틀린 풀이
s = input().split('-')

if len(s) == 1:
    s = s[0]
    # 10+20+30 처럼 +만 있는 경우는 len(s) == 1임
    if s.find('+') != -1:
        temp = list(map(int, s.split('+')))
        print(sum(temp))
    # 아니면 숫자만 주어지는 경우
    else:
        print(s)
else:
    # 55-50+40-40+20-20 = -115
    tempSum = 0
    # s[0]이 10+20 이렇게 더해진 값이 아닐 때 사용되는 flag
    flag = True
    if s[0].find('+') == -1:
        tempSum = int(s[0])
    else:
        tempSum = sum(list(map(int, s[0].split('+'))))
        flag = False
    n = len(s)
    for i in range(n):
        if s[i].find('+') != -1 and flag:
            temp = list(map(int, s[i].split('+')))
            tempSum -= sum(temp)
        # 마지막에 - 인 경우 그냥 -= 해줌
        if s[i].find('+') == -1 and i == len(s)-1:
            tempSum -= int(s[i])
            
    print(tempSum)
'''

s = input().split('-')
num = []
for i in s:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)