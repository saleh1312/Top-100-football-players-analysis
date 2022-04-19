import pandas as pd
import numpy as np
import string 
import re
from HelperFunc import players_scrapper



df=pd.read_excel("data\\top100.xlsx")

pfinder=players_scrapper(link_website="https://www.transfermarkt.us/",link_drive="driver\\chromedriver.exe")

players_info=pd.DataFrame(columns=["name","birth date","age","height","country","pos","foot","current club"
                                   ,"transfer from","transfer to","transfer date"])



for index, row in df.iterrows():
    name=re.sub('[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~’]','',row["Player"]).lower()
    
    row=pfinder.find_player(name, row['Club'])
    players_info=players_info.append(row, ignore_index=True)
    

    
#1- remove sympols , lower
pfinder.close()


players_info.to_excel("data\\top100full.xlsx",index=False)




















