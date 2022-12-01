from fruitmand import fruitmand
for x in range(0, len(fruitmand)):
    if fruitmand[x].get("round") == True:
        print(fruitmand[x].get("name"))