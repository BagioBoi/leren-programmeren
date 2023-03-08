#functionGame
import random

def namegenerator():
    loop = True
    nameListMale = ["Noah", "Lucas", "Sem", "Daan", "Levi", "Liam", "James", "Finn", "Luca", "Milan"]
    nameListFemale = ["Julia", "Mila", "Emma", "Nora", "Olivia", "Sophie", "Tess", "Milou", "Zoë", "Yara"]
    genderInput = input("Bent u een man of een vrouw?: ")
    while loop:
        if genderInput == "man":
            fakeNameInput = input("Wat is je naam?: ")
            name = random.choice(nameListMale)
            namecheck = input(f"Is dit jouw naam {name}?: ")
            if namecheck == "ja":
                loop = False
        elif genderInput == "vrouw":
            fakeNameInput = input("Wat is je naam?: ")
            name = random.choice(nameListFemale)
            namecheck = input(f"Is dit jouw naam {name}?: ")
            if namecheck == "ja":
                loop = False
        else:
            print("Woah die keuze voor gender heb ik helaas niet aangeboden!")
            genderInput = input("Bent u nou een man of een vrouw?: ")
    return (name)