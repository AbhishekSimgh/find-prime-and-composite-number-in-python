"""In this project you have to enter a positive integer range[A,B]and system
Note:Make use of efficient approach to chek prime status  of the number
For example:
Range is(7,10)
Then the status of each number in the range is:
7 is prime
8 is composite or not prime
9 is composite
10 is composite
count:1 prime and 3 composite number in the range.
(student is free to decide the input and output layout for this mini project)
"""
def prime(x):
    c=1
    for i in range(2,x):
        if x%i==0:
            c=0
            break
    return c
#main
a=int(input("enter the starting range: "))
b=int(input("enter the ending range: "))
c,p=0,0
for i in range(a,b+1):
    if i<=0:
        print("please enter a postive number greater then 0")
    elif i==1:
        print("1 is neither prime nor composite its aspecial number")
    else:
        t=prime(i)
        if t==0:
            print(i,"is a composite number")
        elif t==1:
            print(i,"is a prime number")
            p+=1
print("there are",p,"prime number and there are",c,"composite in the range",a,"and",b)
            
                
