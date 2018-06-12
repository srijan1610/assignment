i=0
while(i<10):
    num=input("enter your no")
    print("entered no is "+num)
    i=i+1

#q2

while(True):
    print("infinte")



#q3
num=[]
sq=[]
for i in range(3):
    x=int(input("enter your no"))
    num.append(x)
    sq.append(x*x)
print(num,sq)


#q4

i=0
l=[1,2,"abc",2.0]
a=[]
b=[]
c=[]
for i in l:

    if (type(i)==int):
        a.append(i)
    elif (type(i)==str):
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)

#q5

even=[]
odd=[]
for i in range(1,101):
    if(i%2==0):
        even.append(i)

    else:
        odd.append(i)
print(even)
print(odd)


#6

n=4
for i in range(0,n):
    for a in range(0,i+1):
        print("*",end="")
    print("\r")

#q7

d={'name': 'srijan','age':20}
for i in d:
    print(i,d[i])

#Q8
i=0
c=[]
while(i<5):
    a=int(input("enter number"))
    c.append(a)
    i=i+1
a=int(input("enter number to be searched"))
for i in c:
         if(a==i):
             c.remove(i)
print(c)
