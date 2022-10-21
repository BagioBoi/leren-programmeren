#Kladblok

while True:
    vraag = input("Kan dit in een for loop?").lower
    if vraag == "nee":
        break

for i in range (0, 5):
    print("Goeie for loop hé")

i = 0
while i < 5:
    print("Goeie while loop die op de for loop lijkt")
    i += 1
