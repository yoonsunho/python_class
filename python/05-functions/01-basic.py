num1=5
num2=3
print(num1+num2)

#두 수의 합을 구하는 함수
def  get_sum(num1,num2):
    return num1+num2

#함수를 호출하여 결과 출력
sum_result = get_sum(num1,num2)
print(sum_result)

def make_sum(param1,param2):
    return param1+param2

#함수 호출
result = make_sum(100,30)
print(result)

#함수와 반환값
#print()함수는 반환값이 없다
return_value= print(1) #1
print(return_value) #None

def my_func():
    print('hello')

result = my_func()
print(result) #None #return값이 아니라 print만 호출함

def add_numbers(x,y): #x,y는 매개변수(parameter)
    result = x+y
    return result

a=2
b=3
sum_result = add_numbers(a,b) #a,b는 인자(arguments)
print(sum_result)

