print("####    Oving 6    ####")
print("####  Anders Lima  ####\n")
print("""     

####   Oppgave 1   ####   
""")

def intInput():
    try:
        i=int(input("Skriv inn et heltall: "))
        return i
    except:
        intInput()

def oppg1():
    n=intInput()
    s=0
    cnt=1
    while(s<=n):
        cnt+=1
        s=s+(cnt**2)
    print(s-(cnt**2),cnt-1)
    
oppg1()    
p=input("\nPress ENTER to continue...")

print("\n####   Oppgave 2   ####\n")

li=[1,2,3,4,5,6]

for i in range(0,len(li)):
    if li[i]%2==0:
        li[i]=li[i]*-1

li.sort(reverse=True)

print(li)


p=input("\nPress ENTER to continue...")

print("\n####   Oppgave 3   ####\n")

def vInput():
    inp=input("Skriv in 3 komponenter: ")
    return vakker(inp.split())

def vakker(vec1):
    for i in range(0,len(vec1)):
        vec1[i]=int(vec1[i])
    return vec1

def skalvec(vec1,s):
    for i in range(0,len(vec1)):
        vec1[i]=vec1[i]*s
    return vec1

def vec_len(vec):
    s=0
    for i in range(0,len(vec)):
        s=vec[i]**2
    return s**(1/2)

vec1=vInput()
def print_d():
    s=int(input("Skalar: "))
    v1l=vec_len(vec1)
    print(vec1,v1l)
    vec2=skalvec(vec1,s)
    v2l=vec_len(vec2)
    print(vec2,v2l)
    print(v1l/v2l)

print_d()

def indreprod(vec1,vec2):
    vec=[None]*3
    for i in range(0,len(vec1)):
        vec[i]=vec1[i]*vec2[i]
    return vec

vec2=vInput()
print(indreprod(vec1,vec2))

p=input("\nPress ENTER to continue...")

print("\n####   Oppgave 4   ####\n")

teeth = [
95 , 103 , 71 , 99 , 114 , 64 , 95 , 53 , 97 , 114 ,
109 , 11 , 2, 21 , 45 , 2, 26 , 81 , 54 , 14 ,
118 , 108 , 117 , 27 , 115 , 43 , 70 , 58 , 107]

def tannfe():
    for i in range(0,len(teeth)):
        ore=teeth[i]*50
        v=0
        m20=0
        m10=0
        m5=0
        m1=0
        m0_5=0
        while(ore>0):
            if ore%2000==0:
                m20+=1
                ore-=2000
            elif ore%1000==0:
                m10+=1
                ore-=1000
            elif ore%500==0:
                m5+=1
                ore-=500
            elif ore%100==0:
                m1+=1
                ore-=100
            elif ore%50==0:
                m0_5+=1
                ore-=50
        print(m20,m10,m5,m1,m0_5)
    
tannfe()

p=input("\nPress ENTER to continue...")

print("\n####   Oppgave 5   ####\n")

# vim:set fileencoding=latin-1:
import random # Importerer modulen random (generere tilfeldige tall)

# Funksjon:     pick_sentence
# Beskrivelse:  Plukker ut en tilfeldig tekststreng fra en liste av tekstsetninger
# Input:        En liste av tekststrenger
# Ouput:        En tekststreng
def pick_sentence(sentences):
  return sentences[random.randint(0, len(sentences)-1)]

# Funksjon:     print_sentence
# Beskrivelse:  Skriver ut tre tekststrenger paa ei linje til konsoll.
#               Det skal vaere mellomrom (space) mellom tekststreng en og to.
#               Det skal ikke vaere mellomrom (space) mellom tekststreng to og tre.
# Input:        Tre tekststrenger
# Output:       Ingen
def print_sentence(a,b,c):
    print(a+" "+b+c)


# Funksjon:     intro_text
# Beskrivelse:  Skriver en velkomsttekst til konsoll som skal inneholde:
#               20 linjeskift
#               Setningen: "Hei, jeg heter Eliza og vil gjerne snakke med deg."
#               Setningen: "Ikke start svar med stor bokstav og bruk hele setninger."
#               Setningen: "Skriv 'hade' hvis du vil avslutte samtalen"
#               Setningen: "**************************************************"
#               1 linjeskift
# Input:        Ingen
# Output:       Ingen
def intro_text():
    for i in range(1,20):
        print("\n")
    print("Hei, jeg heter Eliza og vil gjerne snakke med deg.")
    print("Ikke start svar med stor bokstav og bruk hele setninger.")
    print("Skriv 'hade' hvis du vil avslutte samtalen")
    print("**************************************************\n")

# Funksjon:     main
# Beskrivelse:  Hovedfunksjonen i programmet
# Input:        Ingen
# Output:       Ingen
def main():
  # Initialisering av variabler
  answer = "ikke hade" # Soerger for at while-loekka kjoerer foerste gang

  # En liste av spoersmaal
  questions = ['Hva gjoer du', 'Hvordan gaar det', 'Hvorfor heter du',
              'Liker du aa hete', 'Foeler du deg bra', 'Hva har du gjort idag',
              'Hva tenker du om framtida', 'Hva gjoer deg glad', 'Hva gjoer deg trist']

  # En liste av oppfoelgningsspoersmaal
  follow_ups = ['Hvorfor sier du', 'Hva mener du med', 'Hvor lenge har du sagt',
               'Hvilke tanker har du om', 'Kan du si litt mer om',
               'Naar tenkte du foerste gang paa']

  # En liste av responser
  responses = ['Fint du sier det', 'Det skjoenner jeg godt', 'Saa dumt da', 'Foeler meg ogsaa saann',
              'Blir trist av det du sier', 'Saa bra', 'Du er jammen frekk']

  # Skriv velkomsttekst til konsoll vha funksjonen intro_text
  intro_text()

  # Spoer brukeren om navnet og lagre svaret i en variabel
  navn=input("Hva heter du?\n")

  # Programmet kjoerer i loekke helt til brukeren svarer "hade"
  while answer != "hade":
    pass

    # NB: All kode her maa skrives med to innrykk!!!

    # Plukk ut et tilfeldig spoersmaal fra lista questions 
    # ved hjelp av funksjonen pick_sentence
    q=pick_sentence(questions)

    # Skriv spoersmaalet etterfulgt av navnet til brukeren
    # og et spoersmaalstegn ved hjelp av funksjonen print_sentence
    print_sentence(q,navn,"?")

    # Spoer brukeren om et svar med teksten "Svar: " og lagre
    # resultatet i en variabel
    answer=input("Svar: ")

    # Plukk ut et tilfeldig oppfoelgingsspoersmaal fra lista follow_ups 
    # ved hjelp av funksjonen pick_sentence
    fo=pick_sentence(follow_ups)

    # Skriv oppfoelgningsspoersmaalet sammen med svaret fra brukeren
    # og et spoersmaalstegn ved hjelp av funksjonen print_sentence
    print_sentence(fo,answer,"?")
    
    # Spoer brukeren om et svar med teksten "Svar: " uten aa lagre
    # resultatet til variabel
    input("Svar: ")

    # Plukk ut en tilfeldig respons fra lista responses 
    # ved hjelp av funksjonen pick_sentence
    res=pick_sentence(responses)

    # Skriv reponsen sammen med navnet til brukeren
    # og et punktum (".") ved hjelp av funksjonen print_sentence
    print_sentence(res,navn,".")

main()