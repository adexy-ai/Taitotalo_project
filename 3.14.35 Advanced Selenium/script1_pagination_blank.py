# -*- coding: utf-8 -*-
"""
Boolean Data Analytics Course

Web Scraping and Web Interaction with Selenium: 
 in this script we write some code that looks at the pagination 
 of the website; we create a function that, given a page, 
 navigates to that page and scrapes the data contained in a table
 and then appends it to a previously initialised DataFrame 
"""


### GETTING STARTED

# Download the latest stable release of the ChromeDriver
# https://sites.google.com/chromium.org/driver/

# import requred libraries and modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


### DRIVER SETUP

# initialise the driver (and open up a browser window)
driver = webdriver.Chrome()

# open up a specific web page
driver.get("https://www.scrapethissite.com/pages/forms/")


### DEFINE FUNCTION FOR COLUMN LIST CREATION

# since we will need to repeat this process for other 5 variables, 
# let's create a function
def create_col(class_name):
    s_column = driver.find_elements(By.CLASS_NAME, class_name)
    column = [col.text for col in s_column]
    return column


### DEFINE FUNCTION FOR PAGE SCRAPING


#### PAGINATION 

# Identify how many pages of data there are

# Initialise an empty dataframe to contain our data

# Loop through all of the pages and use the scrape page function to append the data to df_teams

    
# Reset the index    

# And finally close the browser
