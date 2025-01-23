num = 0 #전역변수

def increment():
    # print(num)#SyntaxError: name 'num' is used prior to global declaration
    global num
    num +=1

# def increment(num):
#     # SyntaxError: name 'num' is parameter and global
#     global num
#     num +=1
    

print(num) #0
increment()
print(num) #1


