#맴버십 연산자
word='hello'
numbers=[1,2,3,4,5,[6,7,8]]

print('h'in word) #True
print('z'in word) #False

print(4 not in numbers) #False
print(6 not in numbers) #Trud
print([6] in numbers) #False
print([6,7] in numbers) #False
print([6,7,8] in numbers) #True
