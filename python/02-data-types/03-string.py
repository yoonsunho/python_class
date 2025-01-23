print(type('hello world')) #<class 'str'>

#escape sequence
# 철수야'안녕'
print('철수야 \'안녕\'')

'''
이 다음은 엔터
입니다
'''
print('이 다음은 엔터\n입니다')

#String Interpolation "f-string"
bugs ='roaches'
counts = 13
area ='living room'
#Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')

#문자열의 시퀀스 특징
MY_STR='hello'
#1.인덱싱 #e
print(MY_STR[1])

#2. 슬라이싱 
print(MY_STR[2:4])#ll
print(MY_STR[0:3])#hel
print(MY_STR[3:])#lo
print(MY_STR[0:5:2])#hlo #step지정
print(MY_STR[::-1])#olleh #step이 음수일 경우

#3. 길이 
print(len(MY_STR)) #5

#4. 문자열은 불변 (시퀀스 요소 변경할 수 없음)
# TypeError: 'str' object does not support item assignment
#MY_STR[1]='z'

#재할당
MY_STR= 'hzllo'
print(MY_STR) #hzllo