packed_values=1,2,3,4,5
print(packed_values) #(1, 2, 3, 4, 5)

#*을 활용한 패킹
numbers=[1,2,3,4,5]
a,*b,c = numbers
print(a) #1
print(b) #[2, 3, 4]
print(*b) # 2 3 4
print(c) #5


def my_func(*args):
    print(args) # (1,2,3,4,5)
    print(type(args)) #<class 'tuple'>

my_func(1,2,3,4,5)