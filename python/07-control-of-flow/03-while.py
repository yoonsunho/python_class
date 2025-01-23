a=0

while a<3:
    print(a)
    a += 1

print('끝')
# 0
# 1
# 2
# 끝

number = int(input('양의 정수를 입력해주세요:'))
while number <=0:
    if number <0:
        print('음수를 입력함')
    else:
        print('0 을 입력함')
    number = int(input('양의 정수를 입력해주세요:'))
print('good!')

# 양의 정수를 입력해주세요:-2
# 음수를 입력함
# 양의 정수를 입력해주세요:0
# 0 을 입력함
# 양의 정수를 입력해주세요:4
# good!