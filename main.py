import random
import time
import primzahlen

def FoundOddNumber():   #Sucht zufällig eine ungerade 150 stellige Zahl
    global p
    global n
    loop = "true"
    while loop=="true":
        n = random.randint(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
        b = n%2
        if b==1:
            loop="false"
    p = n
    return p            #"p" ist die Variable zum abrufen des Endwerts dieser Funktion
    return n

def FoundSecondNumber(n):   #Sucht sich eine zweite random Nummer die größer als 1 ist und kleiner als "p"(siehe FoundOddNumber)
    global a
    x = n-1
    a = random.randint(2, x)
    return a                #"a" ist die Variable zum abrufen des Endwertes dieser Funktion

def FoundBiggestDivider(n, a):      #diese Funktion sucht den größten teiler der Zahlen von "p" und "a"
    global o
    loop="true"
    while loop=="true":
        y = n//a        #Ergebniss ohne Rest
        d = n%a         #Der Rest der Rechnung
        if (d==0):
            o = a
            loop="false"
            break
        else:
            n = a
            a = d   #"o" ist die Variable, die den letzt verwendeten wert von "a" übernimmt und zur überprüfung an die TestBiggestDivider Funktion schickt
    return o

def TestBiggestDivider(): #Teste zusammen mit der Funktion FoundBiggestDivider ob die zahl "p" eine Primzahl ist. Die Erfolgsquote liegt bei ca. 49%
    loop = "true"
    while (loop=="true"):
        FoundOddNumber()
        FoundSecondNumber(n)
        FoundBiggestDivider(n, a)  #Die Variable "p" hat nun eine 49% Chance, dass sie eine Primzahl ist
        if (o==1):
            loop = "false"
            break

def DividingTest():     # Greift Primzahlen aus einer datei namens primzahle.py ab und wandelt diese um
    global f
    zahlen = primzahlen.zahl    #wichtig: Primzahlen.py und main.py müssen im gleichen Verzeichnis sein
    j = len(zahlen)
    v = 0
    while (v<j):
        s = zahlen[v]
        z = p%s
        if (z==0):
            f = 0
            break
        else:
            f = 1
        v = v + 1
    return f

def ReTest8(p):         # Führt die ersten Test 8 mal durch um eine höhren wahrschenlichkeit, dass das ergebnis eine primzahl ist
    global g
    c = p
    v = 0
    while (v<7):
        x = p-1
        k = random.randint(2, x)
        loop="true"
        while loop=="true":
            y = c//k
            d = c%k
            if (d==0):
                e = k
                loop="false"        #Sucht eine random zahl und testet diese durch wie bei den obigen Tests
                break
            else:
                c = k
                k = d
        if (e==1):
            v = v + 1
            if (v==7):
                g = 1
                break
        else:
            g = 0
            break
    return g


def PrimTest():     #Diese ist die Hauptschleife des Primzahlentests
    loop = "true"
    while (loop=="true"):
        TestBiggestDivider()
        DividingTest()
        if (f==1):
            ReTest8(p)
            if (g==1):
                loop = "false"

PrimTest()
print(p)
