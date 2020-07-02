# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def latest_file():
    r = requests.get('http://www.gep.mtsss.gov.pt/indicadores-covid-19-mtsss')
    soup = BeautifulSoup(r.text, 'html.parser') 
    link = soup.findAll('a', attrs={'href': re.compile('/documents')})[0]
    #changing beautifulsoup object to string
    str_link = str(link)
    #extracting the link from object
    clean_link = re.findall('"([^"]*)"', str_link)[0]
    website = 'http://www.gep.mtsss.gov.pt'
    url = website+clean_link
    #transforming csv into dataframe
    data = pd.ExcelFile(url)
    all_my_sheets = pd.read_excel(data, sheet_name=None)
    #save down all worksheets separately
    for key in all_my_sheets: 
        all_my_sheets[key].to_csv('original_files/%s.csv' %key,index=False)
    return all_my_sheets


if __name__ == '__main__':
    all_my_sheets=latest_file()