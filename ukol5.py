class Polozka:
    def __init__(self, nazev, zanr):
        self.nazev=nazev
        self.zanr=zanr
    def get_info(self):
        return f"{self.nazev}, {self.zanr}"

class Filmy(Polozka):
    def __init__(self, nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka=delka
    def get_info(self):
        return super().get_info()+f",{self.delka}"
    def get_celkova_delka(self):
        return self.delka
    
class Serialy(Polozka):
    def __init__(self, nazev, zanr, pocet_dilu, delka_dilu):
        super().__init__(nazev, zanr)
        self.pocet_dilu=pocet_dilu
        self.delka_dilu=delka_dilu
    def get_info(self):
        return super().get_info()+f",{self.pocet_dilu},{self.delka_dilu}"
    def get_celkova_delka(self):
        return self.delka_dilu*self.pocet_dilu
        
brno=Filmy("Nuda v Brně", "Komedie", 2)
print(brno.get_info())
most=Serialy("Most", "Komedie", 7, 1)
print(most.get_info())

class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno=uzivatelske_jmeno
        self.delka_sledovani=0
    def pripocti_shlednuti(self, delka_sledovane_polozky):
        self.delka_sledovani+=delka_sledovane_polozky

monika=Uzivatel("hahaha_tosemja")
print(monika.delka_sledovani)

monika.pripocti_shlednuti(brno.get_celkova_delka())
monika.pripocti_shlednuti(most.get_celkova_delka())
print(monika.delka_sledovani)