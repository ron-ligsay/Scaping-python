from selenium import webdriver
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option('excludedSwithces',['enable-logging;'])
driver = webdriver.Chrome(options=options)

url = 'https://www.mandaluyong.gov.ph/updates/downloads/?id=7'

driver.get(url)

titles = driver.find_elements("class name", 'title')
name = []
for title in titles:
    name.append(title.text)

description = driver.find_elements("class name", 'desc')
details = []
for detail in description:
    details.append(detail.text)

driver.quit()

df = pd.DataFrame({'Ordinance_No'})
df.to_csv('mandaluyong_ordinance.csv',index=False)

print(df.head())
