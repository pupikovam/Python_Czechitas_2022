baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
Package_number=input("Zadejte, prosím, číslo balíku:")

if Package_number in baliky:
    if  baliky[Package_number]==True: print("Balík byl předán kurýrovi")
    elif baliky[Package_number]==False: print("Balík zatím nebyl předán kurýrovi")
else: print("Číslo není v databázi")