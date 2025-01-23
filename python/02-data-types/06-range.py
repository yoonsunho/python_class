#range(시작값, 끝값, 증가값)

my_range_1=range(5)
my_range_2=range(1,10)
my_range_3=range(5,0,-1)

print(my_range_1) #range(0, 5)
print(my_range_2) #range(1, 10)
print(my_range_3) #range(5, 0, -1)

#리스트로 형 변환시 데이터 확인가능
print(list(my_range_1)) #[0, 1, 2, 3, 4]
print(list(my_range_2)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(my_range_3)) #[5, 4, 3, 2, 1]

#xx
print(list(range(5,1))) #[]
print(list(range(1,5,-1))) # []

#주로 반복문으로 활용
for i in range(1,10) :
    print(i) # 1 2 3 4 5 6 7 8 9 

for i in range(1,10,2) :
    print(i) #1 3 5 7 9