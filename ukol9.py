import pandas

zvirata=pandas.read_csv('adopce-zvirat.csv', sep=';')
print("informace o datasetu:")
print(f"dataset má {zvirata.shape[0]} řádků a {zvirata.shape[-1]} sloupců")

print(f"a má následující sloupce: {zvirata.columns.values}")
print(zvirata.iloc[34].loc[['nazev_en','nazev_cz']])

# bonus

zvirata_index=pandas.read_csv('adopce-zvirat.csv', sep=';', index_col="nazev_cz")
print(zvirata_index.index.is_unique)
zvirata_index=zvirata_index.sort_index()
# zvire_zajmu=input("Schválně, co se stane, když napíšeš 'Outloň váhavý'?")
# print(zvirata_index.loc[zvire_zajmu])