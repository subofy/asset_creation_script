from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = Service('/path/to/chromedriver')
browser = webdriver.Chrome(service=driver)
page_url = 'https://domain.com'
browser.get(page_url)
find_user = browser.find_element(By.ID, 'login_name')
find_passwd = browser.find_element(By.ID, 'login_password')
time.sleep(3)
find_user.send_keys('user_name')
find_passwd.send_keys('login_password')
find_login_button = browser.find_element(By.CLASS_NAME, 'ladda-button')
find_login_button.click()
time.sleep(3)

# select more
find_more_button = browser.find_element(By.CLASS_NAME, 'moreMenu')
find_more_button.click()

# select fixed assets
find_assets = browser.find_element(By.CLASS_NAME, 'h_menu_more_item_span')
find_assets.click()
time.sleep(3)

# select asset ledger
find_sub_assets = browser.find_element(
    By.XPATH, '//span[contains(text(), "资产台账")]')
find_sub_assets.click()
time.sleep(3)

# create new asset
find_new_button = browser.find_element(
    By.XPATH, '//span[contains(text(), "新建")]')
find_new_button.click()

time.sleep(5)
find_asset_number = browser.find_element(
    By.XPATH, '/html/body/div[1]/div[3]/div[5]/div/div/div/div[3]/div/div/div[1]/table/tbody/tr[1]/td[2]/div[1]/div[1]/div/input')
find_asset_number.send_keys('lsfhdsjvsdvb')
find_asset_name = browser.find_element(
    By.XPATH, '/html/body/div[1]/div[3]/div[5]/div/div/div/div[3]/div/div/div[1]/table/tbody/tr[1]/td[2]/div[1]/div[2]/div/input')
find_asset_name.send_keys('27寸显示器')
find_parent_type_click = browser.find_element(
    By.XPATH, '/html/body/div[1]/div[3]/div[5]/div/div/div/div[3]/div/div/div[1]/table/tbody/tr[1]/td[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]')
find_parent_type_click.click()
find_parent_type_click1 = browser.find_element(
    By.XPATH, '/html/body/div[1]/div[3]/div[5]/div/div/div/div[3]/div/div/div[1]/table/tbody/tr[1]/td[2]/div[1]/div[3]/div/div[1]/span/div/div[1]/ul/div/li[3]/div')
find_parent_type_click1.click()
find_asset_price = browser.find_element(
    By.XPATH, '/html/body/div[1]/div[3]/div[5]/div/div/div/div[3]/div/div/div[1]/table/tbody/tr[6]/td[2]/div/input')
find_asset_price.send_keys('1000')
find_save_button = browser.find_element(
    By.XPATH, '/html/body/div[1]/div[3]/div[5]/div/div/div/div[6]/span/div[1]/div/span')
find_save_button.click()
time.sleep(3)
