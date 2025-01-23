fruits = ['apple', 'banana', 'cherry']

#enumerate는 (index,요소) tuple형태로 뱉어냄
for index, fruit in enumerate(fruits):
    print(index, fruit)

"""
0 apple
1 banana
2 cherry
"""

#index의 시작번호를 바꿀 수도 있음
for index, fruit in enumerate(fruits, 3):
    print(index, fruit)

"""
3 apple
4 banana
5 cherry
"""
