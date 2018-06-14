#q1(what is time tuple?)

print("There is a popular time module available in python which provides function for working with time,and for converting"

      " between representations ,the function (time.time()) returns the current system time in ticks since 12 am,january 1,1970(epoch)")



      #"Index   Attribute   values"

      #"o       tm_year     2018"

      #"1       tm_mon      1-12"

      #"2       tm_mday     1-31"

      #"3       tm_hour     0 to 23"

      #"4       tm_min      0 to 59"

      #"5       tm_sec      0 to 61(60 or 61 are leap-seconds"

      #"6       tm_wday     0 to 6"

      #"7       tm_yday     1 to 366"

      #"8       tm_isdst    -1,0,1 where -1 means library determines DST")




#q2
import time
print(time.asctime())


#q3
import datetime
d=(datetime.date.today())
print(d.month)



#q5
import datetime
a='2020/01/15'
d=(datetime.datetime.strptime(a,"%Y/%m/%d"))
print(d.day)

#q6
import time
print(time.asctime(time.localtime()))

#Q7
import math
f=int(input("enter a no."))
print(math.factorial(f))

#q8
import math
a=int(input("enter a no"))
b=int(input("enter a no"))
print(math.gcd(a,b))

#q9
import os
print(os.getcwd)
print(os.environ)
