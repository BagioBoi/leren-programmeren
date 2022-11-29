dageninweek = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

# alledagen = "Alle dagen in de week zijn"
# for x in dageninweek:
#     alledagen += " " + x + ","
# print (alledagen)

werkdagen = "Alle werkdagen in een week zijn"
for x in range (0,5):
    werkdagen += " " + dageninweek[x] + ","
print (werkdagen)

# weekenddagen = "De weekend dagen zijn"
# for x in dageninweek[5:7]:
#     weekenddagen += " " + x + ","
# print(weekenddagen)

# weekomgekeerd = "Alle dagen omgekeerd zijn"
# for x in dageninweek[::-1]:
#     weekomgekeerd += " " + x + ","
# print(weekomgekeerd)

# dagenomgekeerd = "Alle werkdagen omgekeerd zijn"
# for x in dageninweek[4::-1]:
#     dagenomgekeerd += " " + x + ","
# print(dagenomgekeerd)

# weekendomgekeerd = "De weekenddagen omgekeerd zijn"
# for x in dageninweek[7:4:-1]:
#     weekendomgekeerd += " " + x + ","
# print(weekendomgekeerd)