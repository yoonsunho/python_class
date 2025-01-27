# find
text = 'banana'
print(text.find('a')) #1
print(text.find('z')) #-1

# index
print(text.index('a')) #1
# print(text.index('z')) #ValueError: substring not found


# isupper : 모두 대문자인지
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  #True
print(string2.isupper())  #False

# islower : 모두 소문자인지
print(string1.islower())  #False
print(string2.islower())  #False

# isalpha
string1 = 'Hello'
string2 = '123heis98576ssh'
string3='안녕'
print(string1.isalpha())  #True
print(string2.isalpha())  #False
print(string3.isalpha()) #True


# replace
text = 'Hello, world! world world'
new_text1 = text.replace('world','Python')
new_text2 = text.replace('world','Python',1) #앞에 한개만replace
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world
print(text) #Hello, world! world world #원본은 불면 #문자열은 불변

# strip
text = '  Hello, world!  '
new_text = text.strip()
new_text1 = text.strip('world') # 모르겠ㄷ음
print(new_text) #Hello, world!
print(new_text1) # ???? 

# split
text = 'Hello, world!'
words1 = text.split(',')
words2 = text.split() #빈칸기준split
print(words1)  # ['Hello', ' world!']
print(words2)  # ['Hello,', 'world!']


# join
words = ['Hello', 'world!']
#TypeError: sequence item 2: expected str instance, int found
# words = ['Hello', 'world!',3,100] #다 문자열로 바꿔야 join할 수 있음
new_text = '-'.join(words)
print(new_text)  # Hello-world!

# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# title
new_text2 = text.title()
print(new_text2)  # Hello, World!

# upper
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4)  # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!


# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal())
print("'-123'.isdecimal():", '-123'.isdecimal())
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())
