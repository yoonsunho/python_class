items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)

# apple
# banana
# coconut

country ='korea'

for char in country:
    print(char)
# k
# o
# r
# e
# a

for i in range(5):
    print(i) #0 1 2 3 4 

my_dict ={
    'x':10,
    'y':20,
    'z':30
}

#딕셔너리는 반복을 돌리면 key 가 출력됨
for key in my_dict:
    print(key) # x y z
    print(my_dict[key]) #10 20 30


numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i]= numbers[i]*2
print(numbers) #[8, 12, 20, -16, 10]

#중첩 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer,inner)

# A c
# A d
# B c
# B d


elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem) #['A', 'B']  ['c', 'd']

for elem in elements:
    for item in elem:
        print(item) #A B c d