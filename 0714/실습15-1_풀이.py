
word = 'banana'

# 1. 리스트에 담는다

result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        # 리스트에 추가해줘
        result.append(idx)
print(result)

# 2. 그때 그때 출력

result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx, end = ' ')