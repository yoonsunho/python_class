#세트 표현
my_set_1 = set() #{}라하면dict로 인식
my_set_2 = {1,2,3}
my_set_3 = {1,1,1}

print(my_set_1) #set()
print(my_set_2) #{1, 2, 3}
print(my_set_3) #{1}

my_set_1 = {1,2,3}
my_set_2 = {3,6,9}

#합집합
print(my_set_1 | my_set_2) #{1,2,3,6,9}

#차집합
print(my_set_1 - my_set_2) #{1,2}

#교집합합
print(my_set_1 & my_set_2) #{3}
