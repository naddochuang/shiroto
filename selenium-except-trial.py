from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import time

geckodriver_path = r'C:\Users\Admin\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe'

options = Options()
options.headless = True

service = Service(geckodriver_path)
driver = webdriver.Firefox(executable_path=geckodriver_path)

search_terms = pd.read_csv('30-ADB-noAPI.csv', header=None, names=['term'])
results = []

download_dir = r"C:\MyDownloads"  # Specify your download directory


def scrape_and_download(term):
    driver.get('https://pubchem.ncbi.nlm.nih.gov/')

    try:
        search_box = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")
        search_box.click()
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)
        driver.execute_script("window.scrollBy(0, 1030);")
        
        # Scroll and wait for results (you can modify the waiting logic here)
        #driver.execute_script("window.scrollBy(0, 1030);")
        #WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[3]/div[2]/div[3]/div[1]/div[1]/aside[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[3]"))
        #)

        time.sleep(9)  # Adjust the sleep time as needed
        pull_down = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[3]/div[2]/div[3]/div[1]/div[1]/aside[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/div[3]')
        pull_down.click()
        time.sleep(5)
        csv_button = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/main[1]/div[3]/div[2]/div[3]/div[1]/div[1]/aside[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/span[1]')
        csv_button.click()
        time.sleep(5)
        
        # Handle potential download issues (replace with your download logic)
        # current_url = driver.current_url  # Assuming download happens on the same page
        # if "download" not in current_url:
        #     print(f"Download failed for term: {term}")

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error occurred for term {term}: {e}")

for term in search_terms['term']:
    scrape_and_download(term)

driver.quit()
