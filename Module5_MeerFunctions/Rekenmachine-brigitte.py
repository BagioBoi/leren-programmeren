# def optellen(n1, n2):
#     return n1 + n2

# def aftrekken(n1, n2):
#     return n1 - n2

# def vermenigvuldigen(n1, n2):
#     return n1 * n2

# def delen(n1, n2):
#     return n1 / n2

# def ophogen(n1):
#     return n1 + 1

# def verlagen(n1):
#     return n1 -1

# def verdubbelen(n1):
#     return n1 * 2

# def halveren(n1):
#     return n1 / 2

# # ---

# calculator = True
# n1 = -1
# nummer1 = ("e","f","g","h")
# nummer2 = ("a","b","c","d")
# choice = input("Wat wilt u doen?\n A) getallen optellen,\n B) getallen aftrekken,\n C) getallen vermenigvuldigen,\n D) getallen delen,\n E) getal ophogen,\n F) getal verlagen,\n G) getal verdubbelen,\n H) getal halveren?\n").lower()
# while calculator:
#     if n1 >=0:
#         if choice in nummer2:
#             n2 = float(input("Wat is het tweede getal dat u wilt gebruiken? "))
#         if choice in nummer1:
#             n1 = antwoord
#     elif choice in nummer2:
#         n1 = float(input("Wat is het eerste getal dat u wilt gebruiken? "))
#         n2 = float(input("Wat is het tweede getal dat u wilt gebruiken? "))
#     elif choice in nummer1:
#         n1 = float(input("Wat is het getal dat u wilt gebruiken? "))

#     if choice == "a": 
#             antwoord = optellen(n1,n2)
#             print(f"{n1} + {n2} = {antwoord}")
#     elif choice == "b": 
#             antwoord = aftrekken(n1,n2)
#             print(f"{n1} - {n2} = {antwoord}")
#     elif choice == "c": 
#             antwoord = vermenigvuldigen(n1,n2)
#             print(f"{n1} x {n2} = {antwoord}")
#     elif choice == "d":
#             antwoord = delen(n1,n2)
#             print(f"{n1} : {n2} = {antwoord}")
#     elif choice == "e":
#             antwoord = ophogen(n1)
#             print(f"{n1} + 1 = {antwoord}")
#     elif choice == "f":
#             antwoord = verlagen(n1)
#             print(f"{n1} - 1 = {antwoord}")
#     elif choice == "g":
#             antwoord = verdubbelen(n1)
#             print(f"{n1} * 2 = {antwoord}")
#     elif choice == "h":
#             antwoord = halveren(n1)
#             print(f"{n1} : 2 = {antwoord}")

#     choice = input(f"Wat wilt u met het antwoord:{antwoord} doen?\n I) Niks,\n J) Gebruik antwoord.\n").lower()
#     if choice == "i":
#         calculator = False
#     elif choice == "j":
#         n1 = antwoord
#         choice = input("Wat wilt u doen?\n A) getallen optellen,\n B) getallen aftrekken,\n C) getallen vermenigvuldigen,\n D) getallen delen,\n E) getal ophogen,\n F) getal verlagen,\n G) getal verdubbelen,\n H) getal halveren?\n").lower()
#         calculator

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
    print(keuze == ("g" or "h"))
    if keuze == ("e" or "f"):
        n2 = 1
    if keuze == ("g" or "h"):
        n2 = 2
    if n1 == False:
        print("n1")
        n1 = float(input("Welk getal: "))
    if n2 == False:
        print("n2")
        print(n2)
        n2 = float(input("Welk getal: "))
    print(f"n2={n2}")
    if keuze == ("a" or "e"):
        result = addition(n1,n2)
    elif keuze == ("b" or "f"):
        result = subtraction(n1,n2)
    elif keuze == ("c" or "g"):
        result = multiplication(n1,n2)
    elif keuze == ("d" or "h"):
        result = division(n1,n2)
    elif keuze == ("i" or ""):
        quit()

    print(f"Het antwoord is {result}")
    n1 = result
    n2 = False
    firstRound = False