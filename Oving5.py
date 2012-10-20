print("####    Oving 5    ####")
print("####  Anders Lima  ####\n")
print(""" 	

####   Oppgave 1   ####

a)	Den binaere ASCII-verdien av 'A' er 0100 0001 og desimalverdien er 65.  

b)	L i s p
	
c)	Metadata er data om data
	
""")

p=input("Press ENTER to continue...")

print("\n####   Oppgave 2   ####\n")

import os

antall_kvinner=0
antall_menn=0
antall_sosmedier=0
antall_facebook=0
antall_timer_sosmedier=0
loop=True
alder=0
kjonn=""

def main():
	global antall_kvinner
	global antall_menn
	global antall_sosmedier
	global antall_facebook
	global kjonn
	global antall_timer_sosmedier
	global loop
	
	while(loop):
		os.system('CLS')
		print("###  Spoerreondersoekelse om sosiale medier  ###\n\n")
		timer_sosmedier=0
		alder, kjonn = get_alder()
		if loop:
			aktiv_sosmedier = get_aktiv_sosmedier()
			if kjonn=="k":
				antall_kvinner+=1
			if kjonn=="m":
				antall_menn+=1
		
		if loop:
			medlem_facebook = get_face_medlem()
			
			if medlem_facebook:
				antall_facebook+=1
			
		if loop:
			timer_sosmedier = get_timer_sosmedier()
			if aktiv_sosmedier:
				antall_sosmedier+=1

		if loop:
			antall_timer_sosmedier=antall_timer_sosmedier+timer_sosmedier
		
		p=input("\n\nTakk for din deltakelse!\n\n(Trykk ENTER)")
			
	print_values()
		

def get_alder():
	a=str(input("Alder: "))
	if a.isdigit():
		if int(a)<16 or int(a)>25 :
			print("\n\nDu er dessverre ikke innenfor maalgruppen.")
			p=input("\nTrykk ENTER...")
			main()
	else:
		if a=="hade":
			end()
		else:
			print("Vennligst skriv inn et tall..")
			get_alder()

	k=""
	while(k!="m" and k!="k" and k!="hade"):
		k=str((input("Kjoenn (m/k): ")))
		if k=="hade":
			end()
	return a,k

def get_aktiv_sosmedier():
	i=str(input("Bruker du ett eller flere sosiale medier? (Ja/Nei) : ")).lower()
	if i=="ja":
		return True
	elif i=="nei":
		loop=False
		return False
	elif i=="hade":
		end()
	else:
		print("Svar ja eller nei.")
		get_aktiv_sosmedier()

def get_face_medlem():
	if kjonn=="k":
		print("Mellom 55-60% av Facebook sine brukere er kvinner.\nEr du en av disse? ")
	elif kjonn=="m":
		print("Mellom 40-45% av Facebook sine brukere er menn.\nEr du en av disse? ")
	a=str(input("")).lower()
	if a=="hade":
		end()
	elif a=="ja":
		return True
	elif a=="nei":
		return False
	else:
		print("Svar ja eller nei")
		get_face_medlem()
		
def get_timer_sosmedier():
	t=str(input("Hvor mange timer bruker du i snitt daglig paa sosiale medier? : "))
	if t.isdigit():
		return int(t)
	else:
		if t=="hade":
			end()
		else:
			get_timer_sosmedier()

def print_values():
	os.system("CLS")
	print("Resultater:\n")
	print("Antall kvinner:\t\t",antall_kvinner)
	print("Antall menn:\t\t",antall_menn)
	print("Antall sosmedier:\t",antall_sosmedier)
	print("Antall facebook:\t",antall_facebook)
	print("Antall timer:\t\t",antall_timer_sosmedier)
	
def end():
	global loop
	loop=False
	main()

main()
	
p=input("Press ENTER to continue...")


print("\n####   Oppgave 3   ####\n")

def gcd(a,b):
	while(b>0):
		old_b=b
		b=a%b
		a=old_b
	return a

print(gcd(10,20))

def reduce_fraction(a,b):
	f=gcd(a,b)
	return a/f,b/f

print("%.f/%.f" % reduce_fraction(10,20))

p=input("Press ENTER to continue...")

print("\n####   Oppgave 4   ####\n")

def is_leap_year(y):
	if y%400==0:
		return True
	elif y%100==0:
		return False
	elif y%4==0:
		return True
	
	return False

day=["man","tir","ons","tor","fre","loer","soen"]

def weekday_newyear(year):
	y0=year-1900
	cnt=0
	d=0
	while cnt<y0:
		if is_leap_year(1900+cnt):
			d+=1
		d+=1
		cnt+=1
	return (d%7)

for y in range(1900,1920):
	print(y,day[weekday_newyear(y)])

#4b
def is_workday(d):
	for i in range(0,5):
		if day[i]==d:
			return True
	return False
	
def workdays_in_year(year):
	d=weekday_newyear(year)
	cnt=0
	if is_leap_year(year):
		t=366
	else:
		t=365
	for i in range(0,t):
		if is_workday(day[d%7]):
			cnt+=1
		d+=1
	print(year,"har",cnt,"arbeidsdager.")

for i in range(1900,1920):
	workdays_in_year(i)

p=input("Press ENTER to continue...")

print("\n####   Oppgave 5   ####\n")

def fibonacciA(n):
	f1=1
	f2=1
	for i in range(0,n):
		f3=f1+f2
		fn=f3
		f1=f2
		f2=f3
	return fn

def fibonacciB(n):
	if n==0 or n==1:
		return 1
	else:
		return fibonacciB(n-1)+fibonacciB(n-2)
	
def fibonacciC(n):
	for i in range(0,n):
		print(fibonacciB(i))
	
print(fibonacciC(int(input("f:"))))

p=input("Press ENTER to continue...")