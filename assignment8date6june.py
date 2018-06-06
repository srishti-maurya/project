#solution to question number 1
'''
Python's time functions handle time as a tuple of 9 numbers

index	Field	        Values
0	    4-digit year	2008
1	    Month	        1 to 12
2	    Day	            1 to 31
3	    Hour	        0 to 23
4	    Minute	        0 to 59
5	    Second	        0 to 61 (60 or 61 are leap-seconds)
6	    Day of Week	    0 to 6 (0 is Monday)
7	    Day of year	    1 to 366 (Julian day)
8	    Daylight savings	-1, 0, 1, -1 means library determines DST
'''

#solution to question number 2

import time
ti=time.gmtime()
print("Time calculated using asctime():",end="")
print(time.asctime(ti))
print("Time calculated using ctime():",end="")
print(time.ctime(3000))


#solution to question number 3 ,4 and 5
import datetime
from datetime import date
d=date.today()
print(d)
print(d.day)
print(d.month)


#solution to question number 6
import datetime
from datetime import time
now = datetime.datetime.now()
print(now)

#solution to question number 7 and 8
import math
print(math.factorial(5))
print(math.gcd(8,16))

#solution to question number 9 and 10
import os
print(os.name)
print(os.getcwd())
print(os.environ)
