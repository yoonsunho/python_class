#람다 사용전전
def addition(x, y):
    return x + y


result = addition(3, 5)
print(result)  # 8

#람다 사용 후
addition =lambda x , y : x+y
print(addition(3,4))

numbers =[1,2,3,4,5]
squared = list(map((lambda x: x**2),numbers))
print(squared) #[1, 4, 9, 16, 25]