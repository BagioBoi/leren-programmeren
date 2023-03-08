def nameAndAge():
    newName = input("Voer een naam in").lower()
    newAge = input("Voer leeftijd voor de bijbehorende naam in").lower()
    newAge = (int(newAge))
    namesdict = {"name": newName, "age": newAge}
    return namesdict

people = []

while True:
    person = nameAndAge()
    if person["name"] == "stop":
        break
    people.append(person)



print(people)





# nameslist = nameAndAge()
# for dict in nameslist:
#     name = dict["name"]
#     age = dict["age"]
#     print (f"{name} is {age} jaar")