'''
Created on Nov 23, 2016

@author: Raveena
'''
print('Hi')
from selenium import webdriver
#driver= webdriver.Firefox('C:\\Users\\HariTeja\\Desktop\\geckodriver.exe')
driver= webdriver.Chrome('C:\\Users\\HariTeja\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("https://store.nest.com/")
