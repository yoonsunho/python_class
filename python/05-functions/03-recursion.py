# 재귀함수
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

#거듭제곱
def power(base,exp):
    if exp==0:
        return 1
    else:
        return base * power(base,exp-1)
    
print(power(2,10)) #1024


#피보나치 수열
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6)) #8
