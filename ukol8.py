datum_predstaveni=input("Zadejte datum návštěvy kina ve formátu DD.MM.RRRR")
pocet_osob=int(input("Zadejte počet osob"))

from datetime import datetime, timedelta
ISO_datum_predstaveni=datetime.strptime(datum_predstaveni, "%d.%m.%Y")
print(ISO_datum_predstaveni)


if ISO_datum_predstaveni>=datetime(2021, 7, 1) and ISO_datum_predstaveni<=datetime(2021, 8, 10):
    cena=pocet_osob*250
    print(f"datum představení: {datum_predstaveni}, počet osob: {pocet_osob}, cena: {cena} Kč")
elif ISO_datum_predstaveni>=datetime(2021, 8, 11) and ISO_datum_predstaveni<=datetime(2021, 8, 31):
    cena=pocet_osob*180
    print(f"datum představení: {datum_predstaveni}, počet osob: {pocet_osob}, cena: {cena} Kč")
else:
    print("V tomto datu není kino otevřeno")

