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
peugeot=Auta("4A2 3020","Peugeot 403 Cabrio",47534)
skoda=Auta("1P3 4747", "Škoda Octavia", 41253)

zadane_auto=input("Jaké auto si přejete zapůjčit?")
if zadane_auto=="Škoda":
    zadane_auto="skoda"
elif zadane_auto=="Peugeot":
    zadane_auto="peugeot"
else:
    print("Auto není v databázi")
print(zadane_auto.get_info())
print(zadane_auto.obsazenost())
zadane_auto=input("Jaké auto si přejete zapůjčit?")
