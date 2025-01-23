#리스트 표현
my_list_1 = []
my_list_2 = [1,'a',3.5,'b',5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]

my_list =[1,'a',3,'b',5]

#인덱싱
print(my_list[1]) #a

#슬라이싱
print(my_list[2:4]) #[3,'b']
print(my_list[:3]) #[1,'a',3]
print(my_list[3:]) #['b',5]
print(my_list[0:5:2]) #[1,3,5]
print(my_list[::-1]) #[5,'b',3,'a',1] #정렬x, 내림차순x, 오름차순x

#길이
print(len(my_list))#5

list = [1,2,3,'python',['hello','world','!!!']]
print(len(list))
print(list[4][-1]) #!!!
print(list[-1][1][0]) #w

#리스트는 가변 (리스트의 요소 변경,재할당x)
my_list=[1,2,3]
my_list[0]=100
print(my_list) #[100, 2, 3]

#배열의 주소값 id
#같은 list여도 연속적이지 않음 but 규칙적
#시작점 +(index)*8(byte)
#그렇기 때문에 배열 내 몇번째 값을 찾든 시간복잡도는 동일함
a=[1,2,3,4]
print(id(a))
print(id(a[0])) #1897113348400
print(id(a[1])) #1897113348432
print(id(a[2])) #1897113348464
print(id(a[3])) #1897113348496