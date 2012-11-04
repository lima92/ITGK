import os  

def oppg1():
    print("\n####   Oppgave 1   ####\n")
    
    videoer = [
        'http://www.youtube.com/watch?v=oKI-tD0L18A',
        'http://www.youtube.com/watch?v=82LCKBdjywQ',
        'http://www.youtube.com/watch?v=GpNSip5gyKo',
        'http://www.youtube.com/watch?v=rHG-JO8gIGk',
        'http://www.youtube.com/watch?v=ZFngtBIxRPk',
        'http://www.youtube.com/watch?v=OZBWfyYtYQY'
    ]
    
    def short_link(l_li):
        l="http://www.youtube.com/watch?v="
        s="youtu.be/"
        s_li=[]
        for e in l_li:
            s_li.append(e.replace(l,s))
        return s_li
    print(short_link(videoer))

    input("\nPress ENTER to continue...")

def oppg2():
    print("\n####   Oppgave 2   ####\n")
    
    cheeses = { 'cheddar': ('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
                'mozarella': ('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
                'brie': ('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
                'geitost': ('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
                'port salut': ('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
                'camembert': ('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
                'ridder': ('GOMBOS-4', 'B16-3'),
                }
    
    print(cheeses['port salut'])
    
    infected=['A234','A235','B13','B14','B15','C31']
    
    inf_c=set()
    
    for c in cheeses:
        for h in cheeses[c]:
            for e in infected:
                if e in h:
                    inf_c.add(c)
                    
    print(inf_c)
    
    for c in cheeses:
        if c not in inf_c:
            for h in cheeses[c]:
                print(h,'  \t',c)
    
    input("\nPress ENTER to continue...")

def oppg3():
    print("\n####   Oppgave 3   ####\n")
    
    birthdays = {
                    "22 nov": [" Lars ", " Mathias "],
                    "10 des": " Elle ",
                    "30 okt": [" Veronica ", " Rune "],
                    "12 jan": " Silje ",
                    "31 okt": " Willy ",
                    "8 jul": [" Brage ", " Oeystein "],
                    "1 mar": " Nina "
                }
    
    def add_bd_to_date(date, name):
        try:
            birthdays[date].append(name)
        except AttributeError:
            birthdays[date]=[birthdays[date],name]
        except KeyError:
            birthdays[date]=[name]
    
    add_bd_to_date("19 nov", "Anders")
    add_bd_to_date("12 jan", "Nora")
    print(birthdays)
    
    input("\nPress ENTER to continue...")
def oppg4():
    print("\n####   Oppgave 4   ####\n")
    
    def number_of_lines(filename):
        n=0
        f = open(filename,'r')
        for line in f:
            n+=1
        f.close()
        return n
        
    print(number_of_lines('nummer.txt'))
    
    
    def number_freq(filename):
        num_freq = {}
        f = open(filename,'r')
        num = f.readlines()
        for n in num:
            num_freq[n[0]]=num_freq.get(n[0],0)+1
        f.close()
        return num_freq
    
    num_set = number_freq('nummer.txt')
    for e in sorted(num_set):
        print(e+": "+str(num_set[e]))
    
    input("\nPress ENTER to continue...")
def oppg5():
    print("\n####   Oppgave 5   ####\n")
    f = open('poenggrenser_2011.csv','r')
    poeng = f.readlines()
    
    def ant_alle():
        cnt=0
        for e in poeng:
            if e.find("Alle")!=-1:
                cnt+=1
        return cnt
    print(ant_alle())
    
    def snitt_gr():
        cnt=0
        png=0
        for e in poeng:
            if e.find("Alle")==-1:
                png+=float(e.rstrip()[e.find(",")+1:])
                cnt+=1
        return (png/cnt)
    print(snitt_gr())
    
    def max_min():
        max=0
        min=100
        for e in poeng:
            if e.find("Alle")==-1:
                png=float(e.rstrip()[e.find(",")+1:])
                if png>max:
                    max=png
                elif png<min:
                    min=png
        return (min,max)
    
    print(max_min())
    
    input("\nPress ENTER to continue...")

loop=True

def main():
    global loop
    os.system('CLS')
    print("####    Oving 9    ####")
    print("####  Anders Lima  ####\n\t\t\t\t\t\t(0 for aa avslutte)")
    n=int(input("Oppgave nr: "))
    if n==1:
        oppg1()
    elif n==2:
        oppg2()
    elif n==3:
        oppg3()
    elif n==4:
        oppg4()
    elif n==5:
        oppg5()
    elif n==0:
        loop=False   

while(loop):
    try:
        main()
    except Exception as var:
        loop=False
        print(var)
    