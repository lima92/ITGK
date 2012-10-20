print("####    �ving 1    ####")
print("####  Anders Lima  ####\n")
print("####   OPPGAVE 1   ####\n")

import math

pi=math.pi

def polar(r,t):
	x=r*math.cos(t)
	y=r*math.sin(t)
	print("("+str(x)+", "+str(y)+")")

polar(3,pi/2)
polar(2.3,pi/3)
polar(5,0)

print("\n####   OPPGAVE 2   ####\n")


def binom(n,k):
	b=(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
	return b

muligeToPar=(binom(13,2)*math.pow(binom(4,2),2)*binom(11,1)*binom(4,1))

muligePokerhender=2598960

prob=muligeToPar/muligePokerhender

print("Sansynligheten for å få to par i poker er: "+str(prob))


print("\n####   OPPGAVE 3   ####\n")

bPi=4*math.atan(1)
print("Pi er                : "+str(bPi))

bTwoSqrd=math.pow(2,1/2)
print("Kvadratroten av 2 er : "+str(bTwoSqrd))
