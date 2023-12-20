from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

import cfg_dev

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# Login Process
driver.get(f"{cfg_dev.BASE_URL}login/login.asp")

id_input_element = driver.find_element(By.ID, "log_id").send_keys(cfg_dev.USE)
pw_input_element = driver.find_element(By.ID, "login_pw").send_keys(cfg_dev.PWD)
login_button = driver.find_element(By.CLASS_NAME, "bt_login").click()
driver.switch_to.alert.accept()

## booking process
reservation_link_button = driver.find_element(
    By.CSS_SELECTOR, "div[class='quick_area'] > a:first-child"
).click()

# Sample
want_to_go_data = 20240106

reservation_data_button = driver.find_element(
    By.CSS_SELECTOR, f"a[href*='{want_to_go_data}']"
).click()

time.sleep(10)

driver.quit()
