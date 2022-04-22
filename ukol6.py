cesta=input("zadejte cestu k souboru:")
with open(cesta, encoding='utf-8') as vstup:
    auta=vstup.readlines()

print(auta)

auta=[auto.replace(",", ".") for auto in auta]
auta=[auto.split() for auto in auta]
celkem_ujeto=0
for auto in auta:
    auto[1]=float(auto[1])
    celkem_ujeto+=auto[1]

print(celkem_ujeto)