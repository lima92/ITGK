print("####    Oving 2    ####")
print("####  Anders Lima  ####\n")

print(""" 	

####   OPPGAVE 1   ####

a)	To forskjeller paa RAM (Random access memory) og en harddisk er at 
	RAM mister all data naar stroemmen skrus av og at RAM har veldig mye
	raskere lese og skrivehastighet.

b)	Den viktigste forskjellen paa RAM OG ROM er at ROM er read-only 
	memory og kan derfor bare leses fra men ikke skrives til.
	
c)	Fordelen med tilfeldig aksess er at man slipper å "spole" gjennom
	data for aa naa data oaa en plass. Man kan "hoppe" rett inn der 
	dataener lagret. VHS og kasetter er eksempler paa sekvensiell 
	aksess, mens RAM er tilfeldig aksess.

d)	1.	"stuff" er navnet paa funksjonen og x er parameteret 
		funksjonen tar.

	2.	i) 	Mangler kolon etter funksjonshodet.
		ii)	Promten er mellom en enkel-og en dobbel-fnutt. Man maa 
			bruke en av delene
		iii)	Man kan ikke multiplisere en string med et tall.
				y maa konverteres til float.
""")

p=input("Press ENTER to continue...")

print("""

####   Oppgave 2   ####

a)	7 3
	5 4
	5 3
	7 3
	
b)	Foerst skrives "7 3" ut fordi x og y blir redefinert i main(), 
	saa"5 4" fordi x og y faar nye verdier i miks(). "5 3" blir printet
	fordi tull() ikke tar noen argumenter og bruker x og y som ble 
	definert i starten.	"7 3" printes til slutt fordi de bruker 
	veridene som be definert i main().
""")

p=input("Press ENTER to continue...")

print("\n####   Oppgave 3   ####\n\na)")


def main():
	navn=input("Navn paa bilen: ")
	brutto=float(input("Bruttopris paa bilen (kr): "))
	vekt=float(input("Vekt paa bilen (kg): "))
	hp=float(input("Antall hestekrefter paa bilen (hk): "))
	co2=float(input("Antall gram Co2-utslipp paa bilen (gram): "))
	volum=float(input("Motorvolum paa bilen (antall cm^3): "))
	
	beregn_avgift(navn,brutto,vekt,hp,co2,volum)

def beregn_avgift(n,b,v,hp,co2,vol):
	pVekt=b*v*0.00034
	pHp=b*hp*0.00015
	pCo2=b*co2*0.004
	pVol=b*vol*0.00055
	
	netto=format(pVekt+pHp+pCo2+pVol,'.2f')
	
	print("Utsalgspris paa",n,"vil bli",netto,"kr.")

main()

p=input("Press ENTER to continue...")

print("""

b)	Utsalgspris paa Ford Mondeo 1.8 vil bli 249594.00 kr.

	Utsalgspris paa Ford Mondeo 1.0 vil bli 211893.50 kr.

	Utsalgspris paa BMW M5 3.0 vil bli 773682.00 kr.

	Utsalgspris paa BMW M5 1.3 vil bli 523989.00 kr.

""")

p=input("Press ENTER to continue...")

print("\n####   OPPGAVE 4   ####\n")

def far2cel():
	far=float(input("Grader fahrenheit: "))
	cel=format(((5/9)*(far-32)),'.2f')
	print(far,"grader fahrenheit =",cel,"grader celcius.")

far2cel()

p=input("Press ENTER to continue...")