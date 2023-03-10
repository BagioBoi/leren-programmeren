#functionGame
from random import randint
import random
nameListMale = ["Noah", "Lucas", "Sem", "Daan", "Levi", "Liam", "James", "Finn", "Luca", "Milan"]
nameListFemale = ["Julia", "Mila", "Emma", "Nora", "Olivia", "Sophie", "Tess", "Milou", "Zoë", "Yara"]
dogListRaces = ["boxer","herdershond", "bloedhond", "husky", "chihuahua","dobermann", "dwergdashond", "spits", "bulldog", "golden retriever", "harrier", "setter", "labrador", "mopshond", "poedel", "shiba", "terrier", "kat"]


def namegenerator():
    loop = True
    genderInput = input("Bent u een man of een vrouw?:").lower()
    while loop:
        if genderInput == "man":
            fakeNameInput = input("Wat is je naam?: ")
            name = random.choice(nameListMale)
            namecheck = input(f"Is dit jouw naam {name}?:").lower()
            if namecheck == "ja":
                loop = False
        elif genderInput == "vrouw":
            fakeNameInput = input("Wat is je naam?: ")
            name = random.choice(nameListFemale)
            namecheck = input(f"Is dit jouw naam {name}?:").lower()
            if namecheck == "ja":
                loop = False
        else:
            print("Woah die keuze voor gender heb ik helaas niet aangeboden!")
            genderInput = input("Bent u nou een man of een vrouw?: ").lower()
    return name

def plankSquareM(points):
    n1 = randint(1,9)
    n2 = randint(20,50)
    answer = n1 * n2
    answercheck = int(input(f"We hebben een plank van {n1} x {n2} nodig voor het hondenhok aan jouw de vraag hoe groot is deze plank?:"))
    if answercheck == answer:
        print("Goed gedaan je hebt de juiste breedte en lengte van balk gekocht.")
        points += 1
    else:
        print("Ohh helaas ik mag hopen dat we hier nog een beetje een normaal hondenhok van kunnen maken.")
    return points

def dogInput():
    score = 0
    dog = input("Vul hier je hondenras in:").lower()
    if dog in dogListRaces:
        print("Goed gedaan je hebt het antwoord helemaal goed.")
        dogListRaces.remove(dog)
        score += 1
    else:
        print("Helaas deze heb je fout.")   
    return score

def knowledgeDog(points):
    print("Zoals gezegd gaan we vragen of jij meerdere verschillende rassen van honden kent.\n!!!Letop land van afkomst hoeft er niet bij en je moet ze allemaal goed hebben!!!")
    score = dogInput()
    score += dogInput()
    score += dogInput()
    print (f"{score} van de 3 goed")
    if score == 3:
        print("Je hebt de juiste kennis over honden rassen om dit hondenhok te bouwen.")
        points += 1
    else:
        print("Het zal moeilijk worden wanneer je een hondenhok bouwt voor zo'n 'kleine honde of een ENORM beest'.")
    return points

def motivated(points):
    teller = 0
    while teller < 13:
        motivated = input("Ben je gemotiveerd om dit hondenhok te bouwen?:").lower()
        if motivated == "ja":
            teller += 1
        else:
            teller = 0
    notMotivated = input("Ben je niet gemotiveerd om dit hondenhok te bouwen?:").lower()
    if notMotivated == "nee":
        print("Geweldig dit was de motivatie die nodig was om het hondenhok eenmaal neer te zetten.")
        points += 1
    else:
        print("Ik vind het zeer jammer dat je niet gemotiveerd bent om het hondenhok te maken.\nIk denk dat je maar beter opnieuw kan beginnen.")
        points = -10
    return points
