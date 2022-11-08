from random import randint
score = 0
totalrounds = 0
roundsinput = 21 #Dit zorgt ervoor dat het de while loop in gaat voor hoeveel rondes je wilt
print('''In dit spel heb je 10 mogelijkheden om een getal tussen van 1 en tot de 1000 te raden.
Het zal aangeven of het getal hoger of lager is en wanneer je in de buurt bent.''')
while roundsinput >= 21: 
    try: #zorgt ervoor dat er geen letters kan worden ingevoerd 
        roundsinput = int(input("Hoeveel rondes wil je spelen"))
        if roundsinput <= 20 and roundsinput > 0:
            break
        else:
            print("je kan maximaal 20 rondes spelen")
    except:
        print("Dat is geen cijfer")

while roundsinput != totalrounds: #Voert de code uit wanneer die twee niet gelijk zijn
    guessteller = 0
    secretnumber = randint(1, 1000)
    while guessteller <= 9: #Het gaat deze loop in en voert het meerdere keren uit totdat er 10 keer is geraden
        print(secretnumber)
        guessinput = int(input("Welk getal denk je dat het is?: "))
        difference = secretnumber - guessinput #Rekent het absolute getal uit
        if guessinput == secretnumber:
            score += 1
            roundsinput -= 1
            print(f"Goed gedaan je hebt het getal {secretnumber} geraden score +1")
            break
        elif abs (guessinput > secretnumber):
            print("Lager")
        elif abs (guessinput < secretnumber):
            print("Hoger")
        
        if abs(difference) <= 50 and abs(difference) >= 20:
            print("je bent warm")
        elif abs (difference) <= 20:
            print("Je bent HEEEL heet")
        else:
            print("Niet in de buurt")

        guessteller += 1
    if roundsinput == totalrounds:
        print(f"Je totale score was {score}")
        exit()
    end = input("Wil je verder").lower()
    if end in ["nee","no"]:
        print(f"Je totale score was {score}")
        exit()

    
