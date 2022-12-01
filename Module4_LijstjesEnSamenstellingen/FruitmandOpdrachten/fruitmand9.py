from fruitmand import fruitmand
del fruitmand[4]
kleuren = []
for kleur in range (len(fruitmand)):
    if fruitmand[kleur]['color'] not in kleuren:
        kleuren.append(fruitmand[kleur]['color'])
print(kleuren)



# for x in range(0, len(fruitmand)):
#     if  fruitmand[x].get("name") == "druif":

# print(fruitmand[x].get("name"))