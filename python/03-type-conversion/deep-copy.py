#얕은 복사
a="123"
b=a
a=a.replace("1","9")
c =a.replace("1","9")
print(a)
print(c)

a1=[1,2,3,4]  #주소값 1000,1008,1016,1024라 가정
b1=a1
a1[1]=10  #주소값 1008이 2가 아닌 10을 가리키게 바꿔주는거임
print(id(a1))
print(id(b1))

print(a1)
print(b1)

#깊은복사
d=[1,2,3,4]
e=d[:] #재할당으로 주소값 달라지게 됨됨 [:]=> 새로운객체 만듬

print(id(d)) #2091723058304
print(id(e)) #2091723057536