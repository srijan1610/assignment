

#Q1

y=int(input("enter year"))
if(y%400==0):
    print("leap year")
else:
    print("not a leap year")

#q2

l=int(input("enter the length"))
b=int(input("enter the breadth"))
if(l==b):
    print("it is a square")
else:
    print("it is a rectangle")

#q3

y=int(input("enter age of first person"))
z=int(input("enter age of second  person"))
p=int(input("enter age of third person"))
if (y>z and y>p):
    print("%d is the oldest"%(y))
elif (z>y and z>p):
    print("%d is the oldest"%(z))
elif (p>y and p>y):
    print("%d is the oldest"%(p))
else:
    print("all have  the same age")
if (y<z and y<p):
    print("%d is  youngest"%(y))
elif (z<y and y<p):
    print("%d is  youngest"%(z))
elif (p<y and p<z):
    print("%d is  youngest"%(p))
else:
    print("all have the same age")

#q4

point=int(input("enter the points"))
if (point>1 and point<=50):
 print("sorry no prize")
elif (point>51 and point<=150):
 print("congo you won wooden dog")
elif (point>151 and point<=180):
 print("congo you won book")
elif (point>181 and point<=200):
 print("congo you won chocoloates")



#q5

x=int(input("enter units"))
p=x*100
if(p>1000):
    p=p-(.10*p)
print(p)
