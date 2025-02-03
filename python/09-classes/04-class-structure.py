class Circle:

    #클래스 변수
    pi=3.14
    
    #생성자 메서드
    def __init__(self, radius):
        self.radius = radius
        

# 인스턴스 생성
# c1 = Circle() #TypeError: __init__() missing 1 required positional argument: 'radius'
c1 = Circle(1)
c2 = Circle(5)

# 인스턴스 변수(속성)
print(c1.radius) #1
print(c2.radius) #5

# 클래스 변수(속성)
print(c1.pi) #3.14
print(c2.pi) #3.14
