from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import requests
import os
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# user agent
my_user_agent = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)"
options.add_argument(f"user-agent={my_user_agent}")
driver = webdriver.Chrome(options=options)

def parcing(url: str):
    "функция для тестовых парсингов"
    driver.get(url)
    select0 = Select(driver.find_element(By.XPATH, '//*[@id="content"]/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div[1]/select'))
    select = Select(driver.find_element(By.XPATH, '//*[@id="content"]/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/form/div[2]/select'))
    select0.select_by_value('9479')
    select.select_by_value('90')
    table = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[3]/div/div[2]/div/div/div[2]')
    print(type(table), type(table.text))
    ts = table.text.split(' ')
    print(ts)
    
    with open('test_parcing2.txt', 'w', encoding='utf-8') as file0:
        file0.write('')
    for i in table.text:
        with open('test_parcing2.txt', 'a', encoding='utf-8') as file:
            file.write(i)
    time.sleep(66)

def read_file():
    "чтение временного файла"
    list = []
    with open('test_parcing2.txt', 'r', encoding='utf-8') as file:
        for i in file:
            list.append(file.readline())
    print('list = ', list)

url = 'https://funpay.com/chips/193/'
parcing(url)
# read_file()