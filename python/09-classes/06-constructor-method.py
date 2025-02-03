class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        # 둘이 관련 없음을 알아야함. 보통 이름을 맞추는 경향은 있음
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')
        # print(f'안녕하세요 {name}입니다.') #name은 존재하지 않음


person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다. #객체 지향
# Person.greeting(person1) #안녕하세요 지민입니다. #이렇게 잘 쓰지 않음
