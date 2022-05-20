import requests
import pandas

zam_liberec=pandas.read_csv("zam_liberec.csv")
zam_plzen=pandas.read_csv("zam_plzeň.csv")
zam_praha=pandas.read_csv("zam_praha.csv")

zam_liberec["Město"]="Liberec"
zam_plzen["Město"]="Plzeň"
zam_praha["Město"]="Praha"

zam_df=pandas.concat([zam_liberec,zam_plzen,zam_praha], ignore_index=True)

platy_unor2021=pandas.read_csv("platy_2021_02.csv")
zam_df_platy=pandas.merge(platy_unor2021,zam_df, on=["cislo_zamestnance"], how="outer")
print(zam_df_platy)

print(platy_unor2021.shape)
print(zam_df.shape)
print(zam_df_platy.shape)

prumerne_platy=zam_df_platy.groupby("Město")["plat"].mean()
print(prumerne_platy)

# bonus zaměstnanci
nepracující=zam_df_platy[zam_df_platy["plat"].isna()]
print(f"počet ve firmě již nepracujících zaměstnanců je {len(nepracující)}")

ukonceni_zamestnanci=nepracující[["jmeno","prijimeni"]]
print(ukonceni_zamestnanci)

# část projekty
vykazy=pandas.read_csv("vykazy.csv")

print(vykazy.groupby("project")["hours"].sum())

# bonus projekty
vykazy=vykazy.rename(columns={"emloyee_id": "cislo_zamestnance"})
zam_platy_projekty=pandas.merge(zam_df_platy,vykazy, on=["cislo_zamestnance"], how="outer")
print(zam_platy_projekty.groupby(["project","Město"])["hours"].sum())