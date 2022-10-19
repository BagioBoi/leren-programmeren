from functools import total_ordering


nummer = 50
totaal = 50
uitkomst = ""
telling = 0 
while totaal <= 1000:
    nummer += 1
    totaal += nummer
    uitkomst += f" + {nummer}"
    telling += 1
    print(f"{telling}. 50 {uitkomst} = {totaal}")
