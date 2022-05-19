import pandas
import pytemperature

temperature=pandas.read_csv("temperature.csv")

print(temperature.head())

praha=temperature[temperature["City"]=="Prague"]
print(praha)

extremni_teplota_high=80
extremni_teplota_low=-20
nad_80=temperature[temperature["AvgTemperature"]>extremni_teplota_high]
print(nad_80)

podminka_60_Evropa=(temperature["AvgTemperature"]>60) & (temperature["Region"]=="Europe")
print(temperature[podminka_60_Evropa])

podminka_extrem=(temperature["AvgTemperature"]>extremni_teplota_high) | (temperature["AvgTemperature"]<extremni_teplota_low)
print(temperature[podminka_extrem].sort_values("AvgTemperature"))

temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])
print(temperature.head())

# jen jedna bonusova podminka
extremni_teplota_high_cel=30
extremni_teplota_low_cel=-10
podminka_extrem_celsia=(temperature["AvgTemperatureCelsia"]>extremni_teplota_high_cel) | (temperature["AvgTemperatureCelsia"]<extremni_teplota_low_cel)
print(temperature[podminka_extrem].sort_values("AvgTemperatureCelsia"))

# Bonus2
den_zajmu=13
zeme_zajmu="US"
podminka_13_US=(temperature["Day"]==den_zajmu) & (temperature["Country"]==zeme_zajmu)
US_data=temperature[podminka_13_US]
print(US_data)

mesta_zajmu=["Washington", "Philadelphia"]
podminka_mesta=US_data["City"].isin(mesta_zajmu)
print(US_data[podminka_mesta])