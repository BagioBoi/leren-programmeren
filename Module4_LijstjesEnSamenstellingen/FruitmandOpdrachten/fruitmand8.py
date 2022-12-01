from fruitmand import fruitmand
fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2800,
    'color' : 'green',
    'round' : True
})
gewicht = 0
for x in range(0, len(fruitmand)):
    if fruitmand[x].get("weight") >= 0:
        gewicht += fruitmand[x].get("weight")
print (gewicht)
        





# for x in range(0, len(fruitmand)):
#     if fruitmand[x].get("weight") == 2800:
#         print(fruitmand[x].get("name"))
