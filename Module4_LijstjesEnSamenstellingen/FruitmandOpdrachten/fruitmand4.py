from fruitmand import fruitmand
from random import randint
aantal = int(input("Hoeveel stuks fruit wil je hebben"))

# for x in range(len(fruitmand)):
#     print(fruitmand[x]["name"])

for x in range(aantal):
    print(fruitmand[randint(0,7)]["name"])