import pandas as pd
import pycountry_convert as pc



df=pd.read_csv("data\\countries of the world.csv")


print(df.head(10))



def country_to_continent(country_name):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    except:
        return "Other"


print(country_to_continent("China"))


df["Continent"]=df["Country"].apply(lambda x:country_to_continent(x.strip()))

print(df[["Country","Continent"]].head(10))

df.to_excel("data\\countries.xlsx",index=False)