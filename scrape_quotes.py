#Scraping quotes from sample website
#https://quotes.toscrape.com/page/1/

from selenium import webdriver
import csv
import time

csv_writer = csv.writer(open("quotes.csv",'w',encoding='utf-8',newline=''))

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging;'])
driver = webdriver.Chrome(options=options)

url = 'https://quotes.toscrape.com/page/1/'

driver.get(url)
time.sleep(1)

""" quotes = driver.find_element('class name','text')
#print(quotes.text)
author = driver.find_element('class name','author')
#print(author.text)
tags = driver.find_element('class name','tags')
#print(tags.text) """

""" quotes = driver.find_elements('class name','text')
for quote in quotes:
    print(quote.text)
authors = driver.find_elements('class name','author')
for author in authors:
    print(author.text)
tags = driver.find_elements('class name','tags')
for tag in tags:
    print(tag.text) """


for i in range(5):
    quotes = driver.find_elements('class name','text')
    authors = driver.find_elements('class name','author')
    tags = driver.find_elements('class name','tags')

    with open("quotes.csv",'w',encoding='utf-8',newline='') as file:
        for k in range(len(tags)):
            data = [quotes[k].text.strip('\"'),authors[k].text.strip('\"'),tags[k].text.strip('\"')]
            csv_writer.writerow(data)
        next = driver.find_element('xpath','//li[@class="next"]/a')
        next.click()
    file.close()            

driver.quit()