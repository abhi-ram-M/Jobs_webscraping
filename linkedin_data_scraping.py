import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
title = 'Python Developer'
location = 'Toronto'
list_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python%2BDeveloper&location=Toronto&start=25"
response = requests.get(list_url)
list_soup = BeautifulSoup(response.text,'html.parser')
page_jobs = list_soup.find_all('li')
id_list = []
for job in page_jobs:
    base_card_div = job.find('div', class_='base-card')
    job_id = base_card_div.get('data-entity-urn').split(':')[3]
    print(job_id)
    id_list.append(job_id)

#print(response)
for job_id in id_list:

    job_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
    job_response = requests.get(job_url)
    job_soup = BeautifulSoup(job_response.text,'html.parser')
    company_name = job_soup.find('a',class_="topcard__org-name-link topcard__flavor--black-link").text.strip()
    job_role = job_soup.find('h2', class_ = "top-card-layout__title")


    print(company_name)
'''
find posting time in days
use try and except statements for data to handle missing values
'''
