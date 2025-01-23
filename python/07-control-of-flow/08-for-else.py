for i in range(10):
    if i ==5:
        print('다섯번쨰에서 멈췄습미다')
        break
else:
    #만약에 조건문에 들어가지 않고 break하지 않고 끝까지
    #  for loop 돌면 전부 돌았습미다를 출력하시오오
    print('전부 돌았습니다')


flag =False

for i in range(10):
    if i==5:
        print("5번째에서 멈췄습니다")
        flag = True
        break
if flag ==False:
    print('전부 돌았습니다')