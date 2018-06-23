
#Q1
f=open("test1.txt",encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("enter number of lines u want to print"))
for i in range(0,n):
    print(a[i])
f.close()


#Q2

a="love"
f=open("test4.txt","r")
z=f.read()
m=z.split()
print(z.count(a))

#Q3

f=open("test.txt",encoding="utf8")
a=(f.readlines())
c=open("test2.txt","w")
c.writelines(a)


#Q4

i=0
f=open("test2.txt",encoding="utf8")
a=(f.readlines())
b=open("test4.txt",encoding="utf8")
c=(b.readlines())
d= open("test3.txt","w")
for i,j in zip(a,c):
    d.write(i+j)
f.close()
b.close()
d.close()


#q5

import random
obj1=open("test.txt","w")
obj2=open("sorted1.txt","w")
li=[]
lil=[]
str1=""
str2=""
for i in range(10):
    a=random.randint(0,9)
    li.append(a)
for j in li:
    str1="".join(str(j))
    obj1.write(str1+"\n")
obj1.close()
obj3=open("test.txt",encoding="utf8")
str5=obj3.read()
print(str5)
for x in str5:
    if(x.isdigit()):
        str6="".join(x)
        lil.append(str6)
lil.sort()
for k in lil:
    str2="".join(str(k))
    obj2.write(str2+"\n")
obj2.close()
obj3.close()
