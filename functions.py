#q1

def area(a):
    a=3.14*a*a
    return a
x=int(input("enter radius :"))
print("area of circle is %s "%area(x))


#q2

def perfect(i):
    sum=0
    for n in range(1,i):
        if(i%n==0):
            sum=sum+n
            n=n+1
        if(sum==i):
            return True
for i in range(1,1001):
    if(perfect(i)==True):
        print("perfect number is %s" %i)
    i=i+1


#q3

i=1
def table(a,i):
    print(a*i)
    i=i+1
    if(i<=10):
        table(a,i)
table(12,i)


#q4

a=int(input("enter base"))
b=int(input("enter power raised"))
def power(a,b):
    if(b!=0):
        return(n*power(a,b-1))
    else:
        return 1
    print("result is %s" %power(a,b))

#q5

a=int(input("enter number"))
def factorial(a):
    if(a==1):
        return 1
    else:
          return (a*factorial(a-1))
d={}
d={a:factorial(a)}
print(d)


