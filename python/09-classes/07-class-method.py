class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population() #인스턴스 생성할 때마다 클래스 메서드 호출

    @classmethod #클래스 메서드(역할 분리를 위함)
    def increase_population(cls):
        cls.population +=1

person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  #2 #클래스 메서드 두번 호출함

Person.increase_population()
print(Person.population) # 3
 