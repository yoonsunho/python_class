class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)


p1 = Person()
p1.talk()  # unknown #인스턴수 변수 정의 x . 클래스 변수 출력

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown # 인스턴스 변수 정의 x. 클래스 변수 출력
p2.name = 'Kim'
p2.talk()  # Kim # 인스턴스 변수 정의. 인스턴스 변수(Kim) 출력

print(Person.name)  # unknown #클래스 변수 name값이 Kim 으로 변경된것이 아니라
print(p1.name)  # unknown
print(p2.name)  # Kim #p2인스턴스으 변수 name이 Kim 으로 저장됨
