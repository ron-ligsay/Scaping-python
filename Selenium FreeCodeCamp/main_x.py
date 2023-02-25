import os
from selenium import webdriver

#os.environ['PATH'] += "../chromedriver.exe"
driver = webdriver.Chrome()
driver.get()
driver.implicit_wait(30)
#my_element = driver.find_element_by_id('downloadButton')
#my_element.click()
my_second_element = driver.find_element_by_class_name('progress-label')
