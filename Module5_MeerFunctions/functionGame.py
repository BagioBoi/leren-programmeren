#functionGame
from random import randint
import random
nameListMale = ["Noah", "Lucas", "Sem", "Daan", "Levi", "Liam", "James", "Finn", "Luca", "Milan"]
nameListFemale = ["Julia", "Mila", "Emma", "Nora", "Olivia", "Sophie", "Tess", "Milou", "Zoë", "Yara"]
points = 0

def namegenerator():
    loop = True
    genderInput = input("Bent u een man of een vrouw?: ").lower()
    while loop:
        if genderInput == "man":
            fakeNameInput = input("Wat is je naam?: ")
            name = random.choice(nameListMale)
            namecheck = input(f"Is dit jouw naam {name}?: ").lower()
            if namecheck == "ja":
                loop = False
        elif genderInput == "vrouw":
            fakeNameInput = input("Wat is je naam?: ")
            name = random.choice(nameListFemale)
            namecheck = input(f"Is dit jouw naam {name}?: ").lower()
            if namecheck == "ja":
                loop = False
        else:
            print("Woah die keuze voor gender heb ik helaas niet aangeboden!")
            genderInput = input("Bent u nou een man of een vrouw?: ").lower()
    return name

def plankSquareM():
    n1 = randint(1,9)
    n2 = randint(20,50)
    answer = n1 * n2
    try:
        answercheck = int(input(f"We hebben een plank van {n1} x {n2} nodig voor het hondenhok aan jouw de vraag hoe groot is deze plank?: "))
    except:
        print("Dat is geen nummer")
    if answercheck == answer:
        print("Goed gedaan je hebt de juiste breedte en lengte van balk gekocht.")
        global points
        points += 1
    else:
        print("Ohh helaas ik mag hopen dat we hier nog een beetje een normaal hondenhok van kunnen maken.")
    return points
