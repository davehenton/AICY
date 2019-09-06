import random

def FoundOddNumber():   #Sucht eine random Zahl zwischen 10^149 und 999...9(150x)
    global p
    global n            #Und prüft ob diese gerade ist. Wenn nicht beginnt es von vorne
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
            print(p)
            loop = "false"
            break

if __name__ == "__main__":
    TestBiggestDivider()
