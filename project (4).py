import requests
import re # regular expressions
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import pandas as pd

c=0


names = []
journals = []
authors = []
year = []
publisher=[]
cited_by_papers = []
abstract = []
count =1
soups=[]

for i in range(11,13):
    URL =f'https://ieeexplore.ieee.org/search/searchresult.jsp?highlight=true&returnType=SEARCH&matchPubs=true&refinements=ContentType:Journals&returnFacets=ALL&pageNumber={i}'
    CHROME_DRIVER_PATH = r'C:\Users\shah2\Desktop\CSS503\chromedriver.exe'
    s = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=s)
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
    driver.get(URL)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    soups.append(soup)


for i in range(len(soups)):
#    for block in soups[i].findAll('div', attrs={'class':class_title}):
#            name_str = block.find('a').text
 #           names.append(name_str)
  #  for block in soups[i].findAll('div', attrs={'class':'description text-base-md-lh'}):
   #         journal_str = block.find('a').text
    #        journals.append(journal_str)

    follow_loop = range(3, 28)
    for x in follow_loop:
            journal_xpath = "/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div["
            journal_xpath += str(x)
            journal_xpath += "]/xpl-results-item/div[1]/div[1]/div[2]/div/a"
            journal_str = driver.find_element("xpath",journal_xpath).get_attribute('innerHTML')
            journals.append(journal_str)

            names_xpath = "/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div["
            names_xpath += str(x)
            names_xpath += "]/xpl-results-item/div[1]/div[1]/div[2]/h2/a"
            names_str = driver.find_element("xpath",names_xpath).get_attribute('innerHTML')
            names.append(names_str)

            authors_xpath = "/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div["
            authors_xpath += str(x)
            authors_xpath += "]/xpl-results-item/div[1]/div[1]/div[2]/xpl-authors-name-list/p"
            authors_str = driver.find_element("xpath",authors_xpath).text.replace("/n", " ")
            res_str = re.sub(r";\n", " ", authors_str)
            authors.append(res_str)

            year_xpath = "/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div["
            year_xpath += str(x)
            year_xpath += "]/xpl-results-item/div[1]/div[1]/div[2]/div/div[1]/span[1]"
            year_str1 = driver.find_element("xpath",year_xpath).get_attribute('innerHTML')
            year_str = year_str1[(year_str1.rfind(":")+2):]
            year.append(year_str)


            publisher_xpath = "/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div["
            publisher_xpath += str(x)
            publisher_xpath += "]/xpl-results-item/div[1]/div[1]/div[2]/div/div[1]/span[4]/xpl-publisher/span/span/span/span[2]"
            publisher_str1 = driver.find_element("xpath",publisher_xpath).get_attribute('innerHTML')
            publisher_str = publisher_str1[(publisher_str1.rfind(":")+1):]
            publisher.append(publisher_str)


            cited_by_papers_xpath = "/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div["
            cited_by_papers_xpath += str(x)
            cited_by_papers_xpath += "]/xpl-results-item/div[1]/div[1]/div[2]/div/div[2]/span/a"
            cited_by_papers_str1 = driver.find_element("xpath",cited_by_papers_xpath).get_attribute('innerHTML')
            cited_by_papers_str = cited_by_papers_str1[(cited_by_papers_str1.rfind("(")+1):].rstrip(cited_by_papers_str1[-1])
            cited_by_papers.append(cited_by_papers_str)

            abstract_xpath = "/html/body/div[5]/div/div/div/div[3]/div/xpl-root/div/xpl-search-results/main/div[2]/div[2]/xpl-results-list/div["
            abstract_xpath += str(x)
            abstract_xpath += "]/xpl-results-item/div[1]/div[2]/div/span"
            abstract_str = driver.find_element("xpath",abstract_xpath).get_attribute('innerHTML')
            abstract.append(abstract_str)
           
data = {
        'name': names,
        'authors': authors,
        'journal': journals,
        'year': year,
        'publisher': publisher,
        'cited_by_papers': cited_by_papers,
        'abstract': abstract
}

df = pd.DataFrame(data)
df.to_csv('reserches.csv', index=False)

