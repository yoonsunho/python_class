# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person) #{}

# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name')) #Alice
print(person.get('country')) #None
print(person.get('country','unknown')) #unknown
print(person['name']) #Alice
# print(person['country']) #KeyError: 'country'

#keys
person = {'name': 'Alice', 'age': 25}
print(person.keys()) #dict_keys(['name', 'age'])
for item in person.keys():
    print(item) 
    #name
    #age

# values
person = {'name': 'Alice', 'age': 25}
print(person.values()) #dict_values(['Alice', 25])
for item in person.values():
    print(item)
    #Alice
    #25

#items
person = {'name': 'Alice', 'age': 25}
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])
for key,value in person.items():
    print(key,value)
    # name Alice
    # age 25

# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age')) # 25
print(person) # {'name': 'Alice'}
print(person.pop('country','unknown')) #unknown
# print(person.pop('country')) #KeyError: 'country'

# setdefault
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country','korea')) # korea
print(person) #{'name': 'Alice', 'age': 25, 'country': 'korea'}

# update
person = {'name': 'Alice', 'age': 25}
other_person={'name':'jane','country':'KOREA'}
person.update(other_person)
print(person) #{'name': 'jane', 'age': 25, 'country': 'KOREA'}

person.update(name='kelly',age=50,address='SEOUL')
print(
    person
) # {'name': 'kelly', 'age': 50, 'country': 'KOREA', 'address': 'SEOUL'}   





