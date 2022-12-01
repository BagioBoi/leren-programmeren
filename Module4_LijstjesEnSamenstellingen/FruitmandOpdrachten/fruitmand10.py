from fruitmand import fruitmand
from operator import itemgetter
fruitmand = sorted(fruitmand , key = itemgetter("weight", "name"),reverse=True)
for aantal in fruitmand:
        print(aantal.get("weight"),aantal.get("name"))

#Aantal is één stuk fruit.
#Je moet het gewicht en de naam hebben van het stuk fruit