#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 00:42:13 2021

@author: abhishek
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 01:08:27 2021

@author: abhishek
"""
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException
import time


path_to_driver='/home/abhishek/Downloads/chromedriver_linux64/chromedriver'

file=open('/home/abhishek/projects/Scrapping/LinkedIn/config.txt')
lines=file.readlines()
username=lines[0][:-1]
password=lines[1]


browser=webdriver.Chrome(path_to_driver)
browser.get('https://www.linkedin.com/uas/login')

#Auth
elementID=browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)


time.sleep(5)



Name,Company,Location=list(),list(),list()

Header=['Job title','Company','Location']

with open('linkedin.csv','w') as file:
        
        csv_writer=csv.writer(file)
        
        csv_writer.writerow(Header)

#cLICK ON JOBS

#browser.refresh()

try:
    browser.find_element_by_xpath('/html/body/div[7]/header/div[2]/nav/ul/li[3]/a').click()

except NoSuchElementException:
    
    browser.refresh()
    
    time.sleep(5)
    
    browser.find_element_by_xpath('/html/body/div[7]/header/div[2]/nav/ul/li[3]/a').click()

time.sleep(5)

x=browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/section/section[1]/div/div[2]/div[1]/div/div[2]/div/input')

x.send_keys('react')

x.send_keys(Keys.ENTER)

time.sleep(6)

    


Next=browser.find_element_by_class_name('jobs-search-two-pane__pagination')

Next=[i for i in Next.find_elements_by_tag_name('li')]

next_page_length=len(Next)

counter=0

while counter<1000:

    try:
        
        Next_page=browser.find_element_by_class_name('jobs-search-two-pane__pagination')
        
        Next=[i for i in Next_page.find_elements_by_tag_name('li')][counter]
    
    except (IndexError,StaleElementReferenceException) as e:
        
        print("Finished")
        break
    
    Next.click()
    time.sleep(5)
    
    x=browser.find_elements_by_tag_name('li')
    for X in x:
        browser.execute_script("arguments[0].scrollIntoView(true);", X);
    # Get scroll height
    SCROLL_PAUSE_TIME = 0.5
    last_height = browser.execute_script("return document.body.scrollHeight")
    for i in range(3):
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
    
        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    
    link=browser.page_source
    
    soup=BeautifulSoup(link,'html')
    
    Name,Company,Location=list(),list(),list()
    
    for name in soup.find_all("div", {"class": "full-width artdeco-entity-lockup__title ember-view"},"a"):
        Name.append(name.text.strip())
    print(Name)
   
    for company in soup.find_all("div", {"class": "artdeco-entity-lockup__subtitle ember-view"},"a"):
        Company.append(company.text.strip())
    print(Company)
    
    for location in soup.find_all("li", {"class": "job-card-container__metadata-item"}):
        Location.append(location.text.strip())
    print(Location)
    
    Data=list()
    for i in range(len(Name)):
        Data.append([Name[i],Company[i],Location[i]])
        
    
    with open('linkedin.csv','a') as file:
        
        csv_writer=csv.writer(file)
        
        csv_writer.writerows(Data)
    
    time.sleep(10)
    print("Next Page")
    
    counter+=1
