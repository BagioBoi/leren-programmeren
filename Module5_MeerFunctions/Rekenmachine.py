firstRound = True
n1 = False
n2 = False

def addition(n1, n2):
    plus = n1 + n2
    return plus

def subtraction(n1, n2):
    aftrekken = n1 - n2
    return aftrekken

def multiplication(n1, n2):
    keer = n1 * n2
    return keer

def division(n1, n2):
    delen = n1 / n2
    return delen
while True:
    if firstRound:
        keuze = input("Wat wilt u doen\n A) getallen optellen\n B) getallen aftrekken\n C) getallen vermenigvuldigen\n D) getallen delen\n E) getallen ophogen\n F) getallen verlagen\n G) getallen verdubbelen\n H) getallen halveren\n I) programma stoppen\n").lower()
    else:
        keuze = input(f"Wat wil je met het resultaat doen {n1}\n A) getallen optellen\n B) getallen aftrekken\n C) getallen vermenigvuldigen\n D) getallen delen\n E) getallen ophogen\n F) getallen verlagen\n G) getallen verdubbelen\n H) getallen halveren\n I) programma stoppen\n").lower()
    if keuze in ("e", "f"):
        n2 = 1
    if keuze in ("g", "h"):
        n2 = 2
    if n1 == False:
        n1 = float(input("Welk getal: "))
    if n2 == False:
        n2 = float(input("Welk getal: "))

    if keuze in ("a", "e"):
        result = addition(n1,n2)
    elif keuze in ("b", "f"):
        result = subtraction(n1,n2)
    elif keuze in ("c", "g"):
        result = multiplication(n1,n2)
    elif keuze in ("d", "h"):
        result = division(n1,n2)
    elif keuze in ("i", ""):
        quit()

    print(f"Het antwoord is {result}")
    n1 = result
    n2 = False
    firstRound = False