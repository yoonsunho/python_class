# append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
print(my_list.append(4))  #None # append자체의 반환값 없음

# extend
my_list = [1, 2, 3]
my_list.extend([4,5,6])


print(my_list)  # [1, 2, 3, 4, 5, 6]


# append와의 비교
my_list.append([5,6,7]) #list[5,6,7]을 하나의 객체로 취급
print(my_list) #[1, 2, 3, 4, 5, 6, [5, 6, 7]]

#extend뒤에는 iterable만 와야함
# print(my_list.extend(5)) #TypeError: 'int' object is not iterable

# insert
my_list = [1, 2, 3]
my_list.insert(1,5)
print(my_list)  # [1, 5, 2, 3]

# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]

# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1)  #5
print(item2)  #1
print(my_list)  #[2,3,4]


# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []
print(my_list.clear()) #None

# index
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1

# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
counting_number1 = my_list.count(4)
print(counting_number)  # 3
print(counting_number1)  # 0


# reverse #reverse는 논리값
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)  #[9, 1, 8, 2, 3, 1]
print(my_list.reverse())  #None


# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True) #순서를 반대로 해라 
#reverse는 논리값이기 때문에 true로 설정되면각 비교가 역전된 것처럼 리스트 요소를 정렬함
print(my_list)  # [100, 3, 2, 1]
