# add
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.add(4)
print(my_set) #{'c', 1, 2, 3, 'a', 4, 'b'}

my_set.add(4)
print(my_set) #{'c', 1, 2, 3, 'a', 4, 'b'}

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set) #set()

# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
print(my_set) # {'a', 1, 3, 'b', 'c'}

# pop
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element) # 1
print(my_set) # {2, 3, 'b', 'a', 'c'}

# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set) #{'a', 1, 3, 'c', 'b'}

my_set.discard(10) 
print(my_set) #{'a', 1, 3, 'c', 'b'}

#update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1,4,5])
print(my_set) #{1, 2, 3, 4, 5, 'c', 'b', 'a'}

# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) #{0,2,4}
print(set1.intersection(set2)) #{1,3}
print(set1.issubset(set2))#False
print(set3.issubset(set1))#True
print(set1.issuperset(set2))#False
print(set1.union(set2))#{0,1,2,3,4,5,7,9}
