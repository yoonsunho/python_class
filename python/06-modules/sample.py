# import my_math #my_math.py불러와서

# print(my_math.add(2,9)) # 11 #내가 만든 함수 불러올 수 있음

#명시적 관점에선 아래 방법이 더 좋음(모듈명만 불러오기)
from my_package.math.my_math import add
from my_package.statistics import tools

print(add(1,2))
print(tools.mod(1,2))
