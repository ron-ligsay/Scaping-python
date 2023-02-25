from selenium import webdriver
import csv
import time

csv_writer = csv.writer(open('skyscraper_filipino_values.csv','w',encoding="utf-8",newline=''))

options = webdriver.ChromeOptions()
options.add_experimental_option('excludedSwithces',['enable-logging;'])
driver = webdriver.Chrome(options=options)

url = "https://www.skyscrapercity.com/threads/filipino-mentality-behavior-beliefs-traits-and-traditions/"

driver.get(url)

#

for i in range(10):
    users = driver.find_elements
    comments = driver.find_elements()
    dates = driver.find_elements()

    with open('skyscraper_filipino_') as file:
        for k in range(len(users)):
            data = [users[k].text.strip('\"'),comments[k].text.strip('\"'),dates[k].text.strip('\"')]
            csv_writer.writerow(data)

            next = driver.find_element("link text",'Next')
            driver.execute_script('argument[0].click')
            time.sleep(3)
        file.close()