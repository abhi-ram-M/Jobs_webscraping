from fontTools.subset.svg import xpath
from lxml.etree import XPath
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

service = Service("chromedriver.exe")
options = Options()

driver = webdriver.Chrome(service=service,options=options)
driver.get('https://www.naukri.com')
input_search = driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input')
input_search.send_keys('web scraping')
experience = driver.find_element(By.XPATH,'//*[@id="expereinceDD"]')
experience.click()
experience_num = 2
input_experience = driver.find_element(By.XPATH,f'//*[@id="sa-dd-scrollexpereinceDD"]/div[1]/ul/li[{experience_num+1}]')
input_experience.click()
input_location = driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input')
input_location.send_keys('Hyderabad')
search_button = driver.find_element(By.XPATH,'//*[@id="root"]/div[7]/div/div/div[6]')
search_button.click()


WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'styles_jlc__main__VdwtF'))
)
soup = BeautifulSoup(driver.page_source,'lxml')
posting = soup.find_all('div',class_="srp-jobtuple-wrapper")
pages = soup.find_all('div', class_="styles_pages__v1rAK")
if pages:
    html_string = str(pages[0])
    numbers = re.findall(r'/web-scraping-jobs-in-hyderabad-secunderabad(?:-(\d+))?', html_string)
    print([int(i) for i in numbers])
    page_numbers = [int(num) if num else 1 for num in numbers]
    number_of_pages = max(page_numbers)

    print("Number of pages:", number_of_pages)
else:
    print("No pagination div found.")



'''CHANGES THAT NEED TO BE DONE
1.Find all the jobs and make them into csv file along with their links
2.iterate through pages exactly to extract all the jobs
3.Convert the code into oop
'''
