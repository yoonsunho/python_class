# from math import sqrt

# print(sqrt(4)) #2.0

import math
import random
import datetime

print(math.pi) #3.141592653589793
print(math.sqrt(4)) #2.0

#특정 범위 사이의 정수를 임의로 뽑아주는
print(random.randint(1,10))

now= datetime.datetime.now()
print(now) #2025-01-23 09:12:10.572106

help(math)
'''
NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.

        The result is between 0 and pi.

    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
-- More  --
'''