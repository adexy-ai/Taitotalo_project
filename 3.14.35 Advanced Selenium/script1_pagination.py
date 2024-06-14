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

def scrape_page(page):
    # click on first page
    driver.find_element(By.LINK_TEXT, str(page)).click()
    
    # create a list for each column of the table
    names = create_col('name')
    year = create_col('year')
    wins = create_col('wins')
    losses = create_col('losses')
    goals_for = create_col('gf')
    goals_against = create_col('ga')
    
    # create a temporary DataFrame to store the current page
    df_teams_tmp = pd.DataFrame(
        {'names': names, 
         'year': year,
         'wins': wins, 
         'losses': losses, 
         'goals_for': goals_for, 
         'goals_against': goals_against
         })
    
    return df_teams_tmp



#### PAGINATION 

# Identify how many pages of data there arw
s_pages = driver.find_element(By.CLASS_NAME, "pagination")
pages = s_pages.text.split('\n')[:-1]

# Initialise an empty dataframe to contain our data
df_teams = pd.DataFrame([])

# Loop through all of the pages and use the scrape page function to append the data to df_teams
for p in pages: 
    # append (with pd.concat()) the temp DataFrame to the empty one
    df_teams = pd.concat([df_teams, scrape_page(p)])
    
df_teams.reset_index(inplace=True, drop=True)

driver.close()