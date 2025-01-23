a = 3.2 - 3.1
b = 1.2 -1.1

print(a) #0.10000000000000009
print(b) #0.09999999999999987
print (a==b) #False

from decimal import Decimal
c = Decimal('3.2')-Decimal('3.1')
d = Decimal('1.2')-Decimal('1.1')
print(c) #0.1
print(d) #0.1
print(c==d) #True