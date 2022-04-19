import pandas as pd
import numpy as np


df=pd.read_excel("data\\top100full.xlsx")

#print(df.columns)





########################## position
pos_unique=[]
for pos in df["pos"]:
    poss=pos.split(" - ")
    for pos_ in poss:
        if pos_ not in pos_unique:
            pos_unique.append(pos_)
        
#print(pos_unique)
######################### trnsfer from and to
clubs_unique=[]
for clubs in df["transfer from"]:
    for club in eval(clubs):
        if club not in clubs_unique:
            clubs_unique.append(club)

for clubs in df["transfer to"]:
    for club in eval(clubs):
        if club not in clubs_unique:
            clubs_unique.append(club)
#print(clubs_unique)
########################   transfer date
dates_unique=[]
for dates in df["transfer date"]:
    date_unique=[]
    for date in eval(dates):
        date_="20"+date.split("/")[0]
        if date_ not in date_unique:
            date_unique.append(date_)
    dates_unique.append(date_unique)
    
    
    
#print(dates_unique)
##################################
df["transfer date"]=dates_unique
posdf = pd.DataFrame({'pos':pos_unique})
clubsdf = pd.DataFrame({'clubs':clubs_unique})

df.to_excel("data\\top100final.xlsx",index=False)
posdf.to_excel("data\\pos.xlsx",index=False)
clubsdf.to_excel("data\\clubs.xlsx",index=False)




















