#Scope예시
def func():
    num = 20
    print('local',num)

func() #local 20
# print('global',num) #NameError: name 'num' is not defined



# LEGB Rule 퀴즈
a = 1
b = 2


def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)  #10 2 500 #순차적으로 밖으로 나가서 값 채움

    local(500) #여기서 호출하는거임
    print(a, b, c)  #10 2 3


enclosed()

print(a, b)  #1 2