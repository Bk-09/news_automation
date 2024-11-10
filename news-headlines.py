from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path=os.path.dirname(sys.executable) # getting path of the executable we create

now=datetime.now()
#MMDDYYYY
month_day_year=now.strftime("%m%d%Y")  #String from time


website = "https://www.espncricinfo.com/cricket-news"
path = "B:\DevZone\chromedriver-win64\chromedriver.exe"   #path of chromdriver

#Headless-mode
options=Options()
options.headless=True

service=Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)

driver.get(website)
#STORE ALL NEWS TEXT INTO CONTAINER 
containers=driver.find_elements(by="xpath",value='//div[@class="ds-border-b ds-border-line ds-p-4"]')

titles=[]
subtitles=[]
links=[]

for container in containers:
    titles.append(container.find_element(by="xpath",value='//div[@class="ds-border-b ds-border-line ds-p-4"]/a/div/div/div[2]/div/h2').text)
    subtitles.append(container.find_element(by="xpath",value='//div[@class="ds-border-b ds-border-line ds-p-4"]/a/div/div/div[2]/div/p').text)
    links.append(container.find_element(by="xpath",value='//div[@class="ds-border-b ds-border-line ds-p-4"]/a').get_attribute("href"))  
    
df_headlines=pd.DataFrame({
    'title':titles,
    'subtitle':subtitles,
    'link':links
    })

file_name=f'headline-{month_day_year}.csv'
#executable final path
final_path=os.path.join(application_path,file_name) #Joining the two paths n name
df_headlines.to_csv(final_path)

driver.quit()


    





