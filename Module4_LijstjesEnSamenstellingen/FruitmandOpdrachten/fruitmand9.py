from fruitmand import fruitmand
print (fruitmand[6])
for fruit in fruitmand:
        if fruit.get("name") == "druif":
            fruitmand.remove(fruit)
kleuren = []
print(fruitmand)
for kleur in range (len(fruitmand)):
    if fruitmand[kleur]['color'] not in kleuren:
        kleuren.append(fruitmand[kleur]['color'])
print(kleuren)



# for x in range(0, len(fruitmand)):
#     if  fruitmand[x].get("name") == "druif":

# print(fruitmand[x].get("name"))