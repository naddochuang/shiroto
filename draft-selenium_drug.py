import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Path to your Firefox driver (geckodriver)
geckodriver_path = r'C:\Users\Admin\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe'

# Set up the Firefox options
options = Options()
options.headless = True  # Run in headless mode (without GUI)

# Read the search terms from the input file
search_terms = pd.read_csv('trial-DEA.txt', header=None, names=['term'])

# Initialize the Firefox driver
service = Service(geckodriver_path)
driver = webdriver.Firefox(executable_path=geckodriver_path)

results = []

for term in search_terms['term']:
    # Navigate to the search engine (e.g., PubChem)
    driver.get('https://pubchem.ncbi.nlm.nih.gov/')

    # Find the search box, enter the term, and submit the search
    search_box = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")
    search_box.click()
    time.sleep(2)
    search_box.send_keys(term)
    search_box.send_keys(Keys.RETURN)
    driver.execute_script("window.scrollBy(0, 1050);")
    
    # Wait for the results to load
    time.sleep(4)  # Adjust the sleep time as needed
    pull_down = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[3]/div[2]/div[3]/div[1]/div[1]/aside[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[3]')
    pull_down.click()
    time.sleep(2)
    csv_button = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[3]/div[2]/div[3]/div[1]/div[1]/aside[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/span[1]')
    csv_button.click()
    time.sleep(5)



# Close the driver
driver.quit()



