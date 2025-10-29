from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.linkedin.co.uk/jobs/search")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "artdeco-icon.lazy-loaded"))
)

input_element = driver.find_element(By.CLASS_NAME, "artdeco-icon.lazy-loaded")
input_element.click()


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "job-search-bar-keywords"))
)
input_element = driver.find_element(By.ID, "job-search-bar-keywords")
input_element.click()
input_element.send_keys("Data" + Keys.ENTER)



time.sleep(60)

driver.quit()