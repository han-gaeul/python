numbers = ['1', '2', '3']
# 숫자로 바꿔서 쓰고 싶다

# n = int(numbers)
# 리스트를 숫자로 형 변환은 불가능!!
# 다만, 숫자 형태의 문자를 변환할 수는 있음

# 가능하지만 1000개 일때는?
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
new_numbers = [a, b, c]

# 반복문
numbers = ['1', '2', '3']
print(numbers)
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# map
numbers = ['1', '2', '3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2) # <map object at 0x10329bc10> : 이미 함수가 모두 적용된 
print(list(new_numbers_2)) # 리스트로 형 변환해서 보면 바뀌어있음
# 보기 위해서 바꾼 것일 뿐. 반드시 list로 바꿔야 하는 것은 아님

print(new_numbers_2, type(new_numbers_2)) # <map object at 0x102f77c10> <class 'map'>