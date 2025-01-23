numbers =[1,2,3,4,5]

print(numbers) #[1, 2, 3, 4, 5]
print(len(numbers)) #5
print(max(numbers)) #5
print(sum(numbers)) #15
print(sorted(numbers,reverse=True)) #[5,4,3,2,1]

#map
numbers=[1,2,3]
result = map(str,numbers)
print(result) #<map object at 0x00000195434B3FA0> # Python의 map() 함수가 반환하는 map 객체
print(list(result)) #['1', '2', '3']

# #map 활용 
# numbers1 = input().split() # 1 2 3 입력
# print(numbers1) #['1','2','3']

# numbers2 = list(map(int,(input().split()))) # 1 2 3 입력
# print(numbers2) #[1, 2, 3]
# print(map(int,(input().split()))) #<map object at 0x000001B5C7467A60>

# zip
girls = ['jane', 'ashley']
boys = ['peter','jay']
pair = zip(girls, boys)
print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]

#zip활용1
kr_scores=[10,20,30,40]
math_scores=[20,40,50,60]
en_scores=[40,20,30]

for student_scores in zip(kr_scores,math_scores,en_scores):
    print(student_scores) 
    #짝이 안맞으면 짝이 맞을때까지만 출력
    # (10, 20, 40)
    # (20, 40, 20)
    # (30, 50, 30)

#zip활용2
scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]

for score in zip(*scores):
    print(score)

# (10, 40, 20)
# (20, 50, 40)
# (30, 39, 50)