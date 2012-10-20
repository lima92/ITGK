print("####    Oving 7    ####")
print("####  Anders Lima  ####\n")
print("""     

####   Oppgave 1   ####

a)""")
def polynom(x):
    return (x**5-4*x**3+10*x**2-10)

def polynom_derivate(x):
    return (5*x**4-12*x**2+20*x)

def newton(func,deriv,start,treshold,max_iter):
    xn=start
    xn1=xn-(func(xn)/deriv(xn))
    cnt=1
    while(((xn1-xn)**2)**(1/2)>treshold and cnt<=max_iter):
        xn=xn1
        xn1=xn-(func(xn)/deriv(xn))
        cnt+=1
    if cnt<max_iter:
        return xn
    else:
        return False

print(newton(polynom,polynom_derivate,0.01,0.000001,20))

p=input("\nPress ENTER to continue...")

print("\n####   Oppgave 2   ####\n")

#OPPG2

p=input("\nPress ENTER to continue...")

print("\n####   Oppgave 3   ####\n")

#OPPG3

p=input("\nPress ENTER to continue...")

print("\n####   Oppgave 4   ####\n")

#OPPG4

p=input("\nPress ENTER to continue...")

print("\n####   Oppgave 5   ####\n")