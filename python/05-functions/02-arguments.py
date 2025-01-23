#1. Positional Arguments
def greet(name,age):
    print(f'안녕하세요, {name}님! {age}살이군요.')

greet('Alice',25) #안녕하세요, Alice님! 25살이군요.
greet(25,'Alice') #안녕하세요, 25님! Alice살이군요.
# greet('Alice') #TypeError: greet() missing 1 required positional argument: 'age'
    
#2. Default Argument Values
def greet(name,age=40):
    print(f'안녕하세요, {name}님! {age}살이군요.')

greet('Bob') #안녕하세요, Bob님! 40살이군요.
greet('Charlie',33) #안녕하세요, Charlie님! 33살이군요.


#3. keyword arguments
def greet(name,age):
    print(f'안녕하세요, {name}님! {age}살이군요.')

greet(name='Dave',age=35) #안녕하세요, Dave님! 35살이군요
greet(age=22,name='Dave') #안녕하세요, Dave님! 22살이군요.
# greet(age=35,'Dave') #SyntaxError: positional argument follows keyword argument
greet('David',age=20) #안녕하세요, David님! 20살이군요.

#4. arbitrary arguments lists
def calculate_sum(*args):
    print(args) #(1, 23, 3, 44, 5)
    print(type(args)) #<class 'tuple'>

calculate_sum(1,23,3,44,5)

#5.arbitrary keyword argument lists
def print_info(**kwars):
    print(kwars)

print_info(name='eve',age=29) #{'name':'eve','age':29}

#인자의 모든 종류 적용
def func(pos1,pos2,default_arg='default',*args,**kwargs):
    print('pos1:',pos1) #pos1:1
    print('pos2:',pos2) #pos2:2
    print('default_args:',default_arg) #default_args:3
    print('args:',args) #args:(4,5,6)
    print('kwargs:',kwargs) #kwargs:{'key1':'value','key2':'value2'}

func(1,2,3,4,5,6,key1='value',key2='value2')