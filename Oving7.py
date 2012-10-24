print("####    Oving 7    ####")
print("####  Anders Lima  ####\n")
print("""     

####   Oppgave 1   ####

a)""")
import math


def polynom(x):
    return (x**5-4*x**3+10*x**2-10)

def polynom_derivate(x):
    return (5*x**4-12*x**2+20*x)

def polynom2(x):
    return ((1/4)*x**2+math.cos(2*x))

def polynom2_derivate(x):
    return ((1/2)*x-2*math.sin(2*x))

def polynom3(x):
    if x<0:
        return (-math.sqrt(-x))
    else:
        return math.sqrt(x)

def polynom3_derivate(x):
    if x<0:
        return (1/(2*math.sqrt(-x)))
    else:
        return (1/(2*math.sqrt(x)))
    
def newton(func,deriv,start,treshold,max_iter):
    xn=start
    xn1=xn-(func(xn)/deriv(xn))
    cnt=1
    while(math.fabs(xn1-xn)>treshold and cnt<=max_iter):
        xn=xn1
        xn1=xn-(func(xn)/deriv(xn))
        cnt+=1
    if cnt<max_iter:
        return xn
    else:
        return False

print(newton(polynom3,polynom3_derivate,1,0.001,50))

input("\nPress ENTER to continue...")
print("\n####   Oppgave 2   ####\n")

def integral(x):
    return math.e**(-(x**2))

def test(x):
    return 5*(x**4)

def simpsons(func,a,b,h):
    Dx=(b-a)/h
    x0=a
    S=0
    for i in range(0,h+1):
        x=a+(i*Dx)
        if i==0 or i==h:
            S+=func(x)
        elif i%2==0:
            S+=2*func(x)
        else:
            S+=4*func(x)
    return S*(Dx/3)

def simpsons_error(func,a,b,error):
    n=4
    s1=(simpsons(integral,a,b,n))
    n+=4
    s2=(simpsons(integral,a,b,n))
    while math.fabs(s2-s1)>=error:
        n+=4
        s1=s2
        s2=(simpsons(integral,a,b,n))
    print(s2)

#simpsons_error(integral,0,1,1e-8)
        

input("\nPress ENTER to continue...")
#print("\n####   Oppgave 3   ####\n")

#OPPG3

#input("\nPress ENTER to continue...")
print("\n####   Oppgave 4   ####\n")

def is_prime(n):
    primes=[2]
    cnt=2
    while cnt<=math.sqrt(n):
        for i in (0,len(primes)):
            if n%primes[i]==0:
                return False
            else:
                primes.append(cnt)
        cnt+=1
    return True

#for i in range(5):
    print(is_prime(int(input(""))))
    
def separate(numbers,treshold):
    less=[]
    more=[]
    for i in numbers:
        if i<treshold:
            less.append(i)
        else:
            more.append(i)
    return less,more

print(separate([41,452,47,25,425,3,1,2,87,8],60))

def multiplication_table(n):
    x=[].append()
    y=n
    
    
    
input("\nPress ENTER to continue...")
print("\n####   Oppgave 5   ####\n")

def comp(a,b):
    if len(a)!=len(b):
        return False
    for i in range(0,len(a)):
        if a[i]!=b[i]:
            return False
    return True

def rev(a):
    l=len(a)-1
    r=""
    while(l>=0):
        r=r+a[l]
        l-=1
    return r

def is_palin(a):
    b=rev(a)
    if a==b:
        return True
    else:
        return False
    
    
while(True):
    print(is_palin(input()))
