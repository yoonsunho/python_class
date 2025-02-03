class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)  # 5
print(c2.radius)  # 10

# c1의 인스턴스 변수 pi를 생성
c1.pi= 100

print(c1.pi)  #100
print(Circle.pi)  #3.14 #클래스 변수는 변하지 않음

# c2는 인스턴스 변수 pi가 없으므로 클래스 변수 pi를 참조
print(c2.pi)  #3.14

# 인스턴스 변수 호출 순서 
# => 인스턴스 자신 -> 클래스 
