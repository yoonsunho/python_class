packed_values = 1, 2, 3, 4, 5

# 언패킹
a, b, c, d, e = packed_values
print(a, b, c, d, e) #1 2 3 4 5

def my_function(x,y,z):
    print(x,y,z)

names= ['alice','kevin','sally']
my_function(*names) #alice kevin sally

def my_func(x,y,z):
    print(x,y,z)

my_dict ={'x':1,'y':2,'z':3}
my_func(**my_dict) # 1 2 3