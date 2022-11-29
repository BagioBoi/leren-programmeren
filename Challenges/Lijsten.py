# tafel = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# for i in range(1, len(tafel)):
#     print (f"Tafel van {i}")
#     for x in tafel:
#         print(f"{x} * {i} = {x * i}")

lijst = [5, 12, 19, 27, 3]
lijst.append(25)

lijst.remove(12)

lijst.pop(0)

lijst.insert(0, 36)

# print (sum(lijst))
lijst.clear()
for x in range(1, 51):
    lijst.append(x)
print (lijst)