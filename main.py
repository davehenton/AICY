import random
import time
import Output

def FoundOddNumber():   #Sucht zufällig eine ungerade Zahl.
    global p
    global n
    loop = "true"
    while loop=="true":
        n = random.randint(10**149, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
        b = n%2
        if b==1:
            loop="false"
    p = n
    return p            #"p" ist die Variable zum abrufen des Endwerts dieser Funktion
    return n

def FoundSecondNumber(n):   #Sucht zufällig eine zweite Nummer: > 1; < "p"(siehe FoundOddNumber)
    global a
    x = n-1
    a = random.randint(2, x)
    return a                #"a" ist die Variable zum abrufen des Endwertes dieser Funktion

def FoundBiggestDivider(n, a):      #diese Funktion sucht den ggT(p;a)
    global o
    loop="true"
    while loop=="true":
        y = n//a        #Ergebniss ohne Rest
        d = n%a         #Der Rest
        if (d==0):
            o = a
            loop="false"
            break
        else:
            n = a
            a = d   #"o" ist die Variable, die den letzt verwendeten Wert von "a" übernimmt und zur Überprüfung an die TestBiggestDivider Funktion schickt
    print(o)
    return o

def TestBiggestDivider(): #Testet zusammen mit der Funktion FoundBiggestDivider ob die zahl "p" eine Primzahl ist.
    loop = "true"
    while (loop=="true"):
        FoundOddNumber()
        FoundSecondNumber(n)
        FoundBiggestDivider(n, a)  #"p" prim möglich
        if (o==1):
            loop = "false"
            break

def DividingTest():     # Greift Primzahlen aus einer Datei namens Output.py ab und wandelt diese um
    global f
    zahlen = Output.zahl    #Wichtig: Output.py und main.py müssen im gleichen Verzeichnis sein
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

def ReTest8(p):         # Führt die ersten Tests 8 mal durch um eine höhren Wahrschenlichkeit, dass p prim ist zu erhöhen.
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
                loop="false"        #Sucht eine zufällige zahl und testet diese durch wie bei den obigen Tests
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


def PrimTest():     #Dies ist die Hauptschleife des Primzahlentests
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
