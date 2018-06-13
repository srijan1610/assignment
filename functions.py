#q1

def area(a):
    a=3.14*a*a
    return a
x=int(input("enter radius :"))
print("area of circle is %s "%area(x))
'''

#q2

def perfect(n):

   sum=0

   for i in range(1,n):

        if(n%i==0):

            sum=sum+i

   if(sum==n):

         return True

   else:

         return False

for i in range(1,1001):

    if(perfect(i)):

        print(i)


#q3

i=1
def table(a,i):
    print(a*i)
    i=i+1
    if(i<=10):
        table(a,i)
table(12,i)


#q4

def power(a,b):

    if(b==1):

        return a

    else:

        return(a*power(a,b-1))

print(power(6,6))

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
