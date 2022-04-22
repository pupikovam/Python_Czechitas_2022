with open("posta.html", encoding='utf-8') as vstup:
    posta = vstup.read()

import re

posta=posta.replace('\n', ' ')
reg_vyraz_mezery = re.compile(" +")
posta=re.sub(reg_vyraz_mezery, " ", posta)
print(posta)
reg_vyraz_mesta=re.compile("\d{3} \d{2}( [^\d\s!<]+)+( \d+)*")
reg_vyraz_psc=re.compile("\d{3} \d{2}( [^\d\s!<]+)+( \d+)*")
mesta=reg_vyraz_mesta.findall(posta)
psc=reg_vyraz_psc.findall(posta)
print(mesta)
print(psc)
