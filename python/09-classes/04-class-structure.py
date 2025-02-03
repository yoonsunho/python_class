class Circle:

    #클래스 변수(설계도 변수) => 모든 인스턴스가 공유
    pi=3.14
    
    #생성자 메서드 #인스턴스 생성시 자동으로 생성 #변수할당, 초기화 담당
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
