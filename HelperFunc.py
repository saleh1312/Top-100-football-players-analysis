from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
import pickle
import sys


class players_scrapper:
    def __init__(self,link_website,link_drive):
        self.driver = webdriver.Chrome(link_drive)
        self.driver.get(link_website)
        
        print("Please click on 'Accept all' button --> waiting 30 sec untill you press")
        #wait untill pressing " Accept all " annoying button
        time.sleep(30)
    def ww(self,xpath,exite=True,coll=False):
        try:
            if coll ==True:
                
                element = WebDriverWait(self.driver,60).until(
                 EC.presence_of_all_elements_located((By.XPATH, xpath)))
            else:
                element = WebDriverWait(self.driver,60).until(
                 EC.presence_of_element_located((By.XPATH, xpath)))
                
            
            return element
            
        except:
            if exite==True:
                print("not found")
                sys.exit()
            else:
                return None
            
    def find_player(self,name="Mohamed Salah",club="liverbool"):
        text_box=self.ww("//input[@class='tm-header__input--search-field']")
        text_box.clear()
        
        text_box.send_keys(name,Keys.RETURN)
        
        
        player=self.ww("//table[@class='items']/tbody/tr[position()=1]//td[@class='hauptlink']/a[position()=1]",exite=False)
        if player==None:
            return None
        player.click()
        
        
        
        div_data_xpath="//div[@class='large-6 large-pull-6 small-12 columns spielerdatenundfakten']"
        div_data=self.ww(div_data_xpath)
        if div_data!= None:
            birth_date=self.driver.find_element_by_xpath(div_data_xpath+"//span[text()='Date of birth:']//following-sibling::span[1]/a").text
            age=self.driver.find_element_by_xpath(div_data_xpath+"//span[text()='Age:']//following-sibling::span[1]").text
            height=self.driver.find_element_by_xpath(div_data_xpath+"//span[text()='Height:']//following-sibling::span[1]").text
            country=self.driver.find_element_by_xpath(div_data_xpath+"//span[text()='Citizenship:']//following-sibling::span[1]").text
            position=self.driver.find_element_by_xpath(div_data_xpath+"//span[text()='Position:']//following-sibling::span[1]").text
            foot=self.driver.find_element_by_xpath(div_data_xpath+"//span[text()='Foot:']//following-sibling::span[1]").text
        
            ######### transfers ########
            
            trans=self.driver.find_elements_by_xpath("//div[@class='responsive-table']//tbody//tr[@class='zeile-transfer']")

            datet=[]
            fromt=[]
            tot=[]
            for tran in trans:
                season=tran.find_element_by_xpath(".//td[position()=1]").text
                clubfrom=tran.find_element_by_xpath(".//td[position()=5]/a").text
                clubto=tran.find_element_by_xpath(".//td[position()=8]/a").text
                datet.append(season)
                fromt.append(clubfrom)
                tot.append(clubto)
                
            return {'name':name,"birth date":birth_date,"age":age,"height":height,
                    "country":country,"pos":position,"foot":foot,"current club":club,
                    "transfer from":list(reversed(fromt)),
                    "transfer to":list(reversed(tot)),
                    "transfer date":list(reversed(datet))}
    

    def close(self):
        self.driver.quit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            