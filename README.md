# Top 100 football players analysis
 analysing top 100 football players 
#
#
#
## First step (scrapping informations of the players)

### codes files: code.py , HelperFunc.py

### files in : driver\chromedriver.exe , data\top100.xlsx

### files out : data\top100full.xlsx
#
#
#
## Second step (adding continents to countries)

### codes files : add cont.py

### files in : data\countries of the world.csv

### files out : data\countries.xlsx
#
#
#
## Third step (extract dimentional tables) -> tables like clubs, and make some edits

### codes files : extract dim tables.py

### files in : data\top100full.xlsx

### files out : data\top100final.xlsx , data\pos.xlsx, data\clubs.xlsx
#
#
#
## Fourth step (analysing)

### codes files : Dashboard.xslx

### files in : data\top100final.xlsx , data\pos.xlsx, data\clubs.xlsx ,data\countries.xlsx
#
#
#
## fifth step (adding frequency of the positions)

### codes files : add_field.py

### files in : Dashboard.py.xlsx,images in assets
#
#
### DashBoard
![alt text](https://github.com/saleh1312/images-githup/blob/main/imgs/top100.jpg?raw=true)
