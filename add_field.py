import xlwings as xw
import cv2
import numpy as np
import pandas as pd
import os



wb = xw.Book("Dashboard.xlsx")
sheet=wb.sheets["tables"]
rng=sheet.range("H7").expand().options(pd.DataFrame).value




pos={'Goalkeeper':[0,(265,859),(255,255,255),1.6],
      'Right-Back':[0,(520,680),(255,255,255),1.6],
      'Centre-Back':[0,(285,720),(255,255,255),1.6], 
      'Left-Back':[0,(55,680),(255,255,255),1.6], 
      
      'Defensive Midfield':[0,(245,584),(0,0,0),1.6],
      'Right Midfield':[0,(520,475),(0,0,0),1.6], 
      'Central Midfield':[0,(320,456),(0,0,0),1.6],
      'Left Midfield':[0,(55,470),(0,0,0),1.6], 
      'Attacking Midfield':[0,(240,315),(0,0,0),1.6],
      
      'Second Striker':[0,(360,205),(255,255,255),1.6], 
      'Right Winger':[0,(527,171),(255,255,255),1.6],
      'Centre-Forward':[0,(230,104),(255,255,255),1.6],
      'Left Winger':[0,(54,175),(255,255,255),1.6]
      }



pos_index=list(pos.keys())


for row in rng.iterrows():
    if row[0] in pos_index:
        pos[row[0]][0]=int(row[1]["count"])


img=cv2.imread("assets\\final_field.jpg")
for key , item in pos.items():
    img=cv2.putText(img,str(item[0]),item[1],cv2.FONT_HERSHEY_SIMPLEX,
                    item[3],item[2],thickness=3)
    

cv2.imwrite(r'assets\position_analysis.jpg', img)




dash_sheet=wb.sheets("dashboard")
rng=dash_sheet.range("L8")

dash_sheet.pictures.add(os.getcwd()+'\\assets\\position_analysis.jpg',
                            name="my_image",update=True,
                            top=rng.top, left=rng.left,width=360,height=450)

























