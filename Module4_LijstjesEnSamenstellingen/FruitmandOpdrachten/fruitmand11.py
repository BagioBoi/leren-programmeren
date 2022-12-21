from fruitmand import fruitmand
kleuren = []
for kleur in range (len(fruitmand)):
    if fruitmand[kleur]['color'] not in kleuren:
        kleuren.append(fruitmand[kleur]['color'])

print(f"Je kan kiezen uit deze kleuren {kleuren}")
while True:
    kleurenInput = input("Welke kleur wilt je kiezen").lower()

    if kleurenInput in kleuren:
        print("Deze kleur zit in de fruitmand")
        break
    else:
        print("Dit is geen geldige kleur")

rond, nietRond, welRond = 0, 0, 0

for x in range(len(fruitmand)):
    kleuren = fruitmand[x].get("color")
    if kleuren == kleurenInput:
        if fruitmand[x].get("round"):
            rond += 1
            welRond += 1
        else:
            rond -= 1
            nietRond += 1
            
print(f"{rond} rond, {nietRond} niet rond, {welRond} wel rond")

if welRond > nietRond:
    print(f"Er zijn {rond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleurenInput}")
elif nietRond > welRond:
    print(f"Er zijn {rond} minder ronde vruchten dan ronde vruchten in de kleur {kleurenInput}")
else:
    print("Er zijn evenveel ronde vruchten bij deze gekozen kleur")