import csv

from bs4 import BeautifulSoup
import requests
import re

with open('times_jobs.csv', 'w') as tb_file:
    writer = csv.writer(tb_file)
    writer.writerow(['Company Name', 'Required Skills', 'Published Date', 'Description And link'])
    for page_no in range(0,6):
        if page_no == 0:
            html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=0DQT0Artificial%20Intelligence0DQT0,0DQT0Machine%20Learning0DQT0,0DQT0Advanced%20SQL0DQT0&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=0DQT0Artificial%20Intelligence0DQT0,0DQT0Machine%20Learning0DQT0,0DQT0Advanced%20SQL0DQT0,&searchBy=0&rdoOperator=OR&txtLocation=hyderabad').text
        else:
            html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=0DQT0Artificial%20Intelligence0DQT0,0DQT0Machine%20Learning0DQT0,0DQT0Advanced%20SQL0DQT0&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=0DQT0Artificial%20Intelligence0DQT0,0DQT0Machine%20Learning0DQT0,0DQT0Advanced%20SQL0DQT0,&searchBy=0&rdoOperator=OR&txtLocation=hyderabad&pDate=I&sequence={page_no}&startPage=1').text
        soup = BeautifulSoup(html_text,'lxml')
        jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
        for job in jobs:
            published_date = job.find('span', class_='sim-posted').text.replace('\n', '')
            #FILTERING BASED ON PUBLISHED DATE
            jobs_data = []
            if 'few' in published_date:

                company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','').replace('\n','').strip()
                skills_uncleaned = job.find('div',class_='more-skills-sections').text.strip().replace('\n\n',',').replace('\n','')
                skills = re.sub(r'\s*,\s*', ', ', skills_uncleaned)
                job_description = job.header.a['href']
                experience = job.find('i', class_="srp-icons experience").parent.text
                jobs_data= [company_name,skills,published_date,job_description]

                print(f"Company Name = {company_name}")
                print(f"Required Skills = {skills}")
                print(f"Published Date = {published_date}")
                print(f"Job description and link = {job_description}\n")
                writer.writerow(jobs_data)
'''
CHANGES THAT NEED TO BE DONE 
1. filter through making changes in the url 
2. make experience into a list of numbers and later filter through that
3. add a clear method to csv so that every time we restart the program we can clear all the existing data
'''




