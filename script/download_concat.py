
import pandas as pd
import time
import requests

start = time.time()
page_no_range = 50

table_list =[]

for page_no in range(page_no_range):
    response = requests.get(f"https://www.themuse.com/api/public/jobs?page={page_no}")
    data = response.json()

    #publication date, job name, job type, job location, company name
    table = pd.DataFrame()

    name_list = []
    company_name_list = []
    job_type_list = []
    publication_date_list =[]
    job_city_list = []
    job_country_list = []


    for i in data['results']:
        publication_date_list.append(pd.to_datetime(i['publication_date'][0:10]).date())
        job_type_list.append(i['type'])
        name_list.append(i['name'])
        company_name_list.append(i['company']["name"])
        try:
            city, country = i['locations'][0]['name'].split(', ')
        except:
            city ='N/A'
            country = (i['locations'][0]['name']) if len(i['locations']) > 0 else 'N/A'

        job_city_list.append(city)
        job_country_list.append(country)

    table['publication_date'] = publication_date_list
    table['job_type'] = job_type_list
    table['name'] = name_list
    table['company_name'] = company_name_list
    table['city']= job_city_list
    table['country'] = job_country_list

    table_list.append(table)

final_table = pd.concat(table_list,ignore_index=True)

final_table.to_excel('/Users/yangliu/Desktop/Data Engineering/Linux/learning/json_practice/docs/final_table.xlsx') 

end = time.time()

print('Time taken: ', end-start)