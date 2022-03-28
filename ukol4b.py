class Auta:
    def __init__(self, spz, znacka_typ, najete_km):
        self.spz=spz
        self.znacka_typ=znacka_typ
        self.najete_km=najete_km
        self.obsazenost=True
    def pujc_auto(self):
        if self.obsazenost==True:
            self.obsazenost=False
            return "Potvrzuji zapůjčení vozidla"
        else: 
            return "Vozidlo není k dispozici"
    def get_info(self):
        return f"{self.spz} {self.znacka_typ}"
    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.obsazenost=True
        self.najete_km=stav_tachometru
        if pocet_dni<=7:
            cena=400*pocet_dni
        elif pocet_dni>7:
            cena=400*pocet_dni
        return f"Cena za zapůjčení auta je {cena} Kč"
peugeot=Auta("4A2 3020","Peugeot 403 Cabrio",47534)
skoda=Auta("1P3 4747", "Škoda Octavia", 41253)

zadane_auto=input("Jaké auto si přejete zapůjčit?")
def pujceni(zadane_auto):
    if zadane_auto=="Škoda":
        print(skoda.get_info())
        print(skoda.pujc_auto())
    elif zadane_auto=="Peugeot":
        print(peugeot.get_info())
        print(peugeot.pujc_auto())
    else:
        print("Auto není v databázi")
pujceni(zadane_auto)
print(peugeot.vrat_auto(150,8))
# pro testování vícenásobného půjčení
#pujceni(zadane_auto)
