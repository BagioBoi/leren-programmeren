from fruitmand import fruitmand
for x in range(0, len(fruitmand)):
    if fruitmand[x].get("name") == "appel":
        print(fruitmand[x].get("weight"))