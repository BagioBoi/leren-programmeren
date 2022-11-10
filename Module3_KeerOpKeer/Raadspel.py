from random import randint
score = 0
total_rounds = 0
guess_input = 0
rounds_input = 21 #Dit zorgt ervoor dat het de while loop in gaat voor hoeveel rondes je wilt
print('''In dit spel heb je 10 mogelijkheden om een getal tussen van 1 en tot de 1000 te raden.
Het zal aangeven of het getal hoger of lager is en wanneer je in de buurt bent.''')
while rounds_input >= 21 or rounds_input <= 0: 
    try: #zorgt ervoor dat er geen letters kan worden ingevoerd 
        print("je kan maximaal 20 rondes spelen")
        rounds_input = int(input("Hoeveel rondes wil je spelen"))
    except:
        print("Dat is geen cijfer")

while total_rounds < rounds_input: #Voert de code uit wanneer die twee niet gelijk zijn
    guess_teller = 0
    secret_number = randint(1, 1000)
    while guess_teller <= 9: #Het gaat deze loop in en voert het meerdere keren uit totdat er 10 keer is geraden
        try: #ik heb try gebruikt zodat je niet per se een antwoord hoeft te geven en hij helemaal afsluit
            guess_input = int(input("Welk getal denk je dat het is?: "))
        except:
            print("Dat is geen cijfer")
        difference = secret_number - guess_input #Rekent het absolute getal uit
        if guess_input == secret_number:
            score += 1
            total_rounds += 1
            print(f"Goed gedaan je hebt het getal {secret_number} geraden score +1")
            break
        elif abs (guess_input > secret_number): #Hier staat de code of je hoger meot raden of lager
            print("Lager")
        elif abs (guess_input < secret_number):
            print("Hoger")
        
        if abs(difference) <= 50 and abs(difference) >= 20: #Hier gebruik ik de variabele difference die heirvoor is uitgerekend om te kijken hoever je van het te raden getal af bent
            print("je bent warm")
        elif abs (difference) <= 20:
            print("Je bent HEEEL heet")
        else:
            print("Niet in de buurt")

        guess_teller += 1 #dit zit aan het einde van de loop en zorgt ervoor dat je 10x kan raden
    end = input("Wil je verder").lower() #Hier stelt het de vraag na iedere ronde of je nog een ronde wilt spelen
    if end in ["nee","no", "n"]:
        break 
print(f"Je totale score was {score}")