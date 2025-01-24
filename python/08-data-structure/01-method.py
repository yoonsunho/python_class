print(type('1')) #<class 'str'>
print((type([1,2]))) #<class 'list'>
print(help(str))

def add(a,b):
    return a+b

class Calculator:
        def add(self,a,b):
                return a+b
    
#함수 호출

add(1,2)

#메서드 호출
a= Calculator()
a.add(1,2)
