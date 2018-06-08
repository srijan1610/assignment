#q1

t=(1,2,"abc")
print(len(t))

#q2
t=(2,3,4,5,6,7)
print(max(t))
print(min(t))

#q3

l=(1*2*3,2*1*1,4*5*6)
print(l)

#sets
#q4
s1=set((7,8,9,10))
s2=set((2,3,4,5))
t=s1-s2
print(t)

#2
l=s2<=s1
print(l)
x=s2>=s1
print(x)

#3
c=s1&s2
print(c)

#dictionries
#q1
a=input("enter name")
b=input("enter marks")
c={'name':a,'marks':b}
print(c)

#q3
f=("mississippi")
i=f.count("m")
j=f.count("i")
k=f.count("s")
h=f.count("p")
e={'no. of m':i,'no, of i':j,'no. of s':k,'no. of p':h}
print(e)