print("####    Oving 3    ####")
print("####  Anders Lima  ####\n")

print(""" 	

####   Oppgave 1   ####

a)	Et hoeynivaa programeringspraak er et lett forstaaelig spraak som
	f.eks. Java, C#, C++, Python osv. Et hoeynivaa spraak oversettes
	til et lavinivaaspraak(assemblerkode/maskinkode) som inneholder
	innstrukser til hvor data er lagret i minnet osv. men som
	forsatt er leselig
	  

b)	Program counter forteller hvor i minnet instruksjonen til den neste
	operasjonen som skal utfoeres ligger.
	
c)	Kompilering er oversettelsen av et hoeyerenivaaspraak til et lavere.
	
""")

p=input("Press ENTER to continue...")

print("\n####   Oppgave 2   ####\n)")


debug = False

def add(a,b):
	if debug:
		print("Input:",a,b)
	s=a+b
	print(s)

t1=int(input("Tall 1: "))
t2=int(input("Tall 2: "))

add(t1,t2)

p=input("Press ENTER to continue...")


print("\n####   Oppgave 3   ####\nb)\n")

import math
pi=math.pi

def sirkel(r):
	O=2*pi*r
	A=pi*r**2
	
	print("Areal:",format(A,'.2f'),"\nOmkrets:",format(O,'.2f'))

sirkel(10)

print("""

c)	10 er et argument, fordi det er data som blir matet inn
	i funksjonen. Et parameter er variabelen funksjonen mottar
	og bruker, i dette tilfellet 'r'.
	
d)	Programmet vil skrive ut: 4 og saa 1. Dette er fordi funksjonen
	foo(a) tar argumentet 2 og bruker det videre som a. 1 printes
	ut av den siste linja fordi a er definert som 1 og endres ikke
	av funsksjonen foo().

""")

p=input("Press ENTER to continue...")

print("\n####   Oppgave 4   ####\n")

def priskat(a):
	if a<5:
		k="Smaabarn:"
		p=0
	elif (a>4 and a<16):
		k="Barn:"
		p=10
	elif (a>15 and a<21):
		k="Ungdom:"
		p=20
	elif (a>20 and a<26):
		k="Student:"
		p=30
	elif (a>24 and a<61):
		k="Voksen:"
		p=40
	elif a>60:
		k="Honnoer:"
		p=0
	else:
		print("input",a,"is illegal")
	
	if p==0:
		p="Gratis"
	
	print("Pris for",k,p)
	
alder=int(input("Alder: "))
priskat(alder)
	

p=input("Press ENTER to continue...")

print("\n####   Oppgave 5   ####\n")

def andregrad(a,b,c):
	d=b**2-4*a*c
	if d==0:
		print("Ligningen "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" = 0 har en(1) reell dobbelrot")
	elif d>0:
		print("Ligningen "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+"  3=0 har to reelle loesninger")
	elif d<0:
		print("Ligningen "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" = 0 har to imaginaere loesninger")
	else:
		print("ERROR")

a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))

andregrad(a,b,c)
	
p=input("Press ENTER to continue...")