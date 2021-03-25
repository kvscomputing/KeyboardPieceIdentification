from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


def scrapeWebsite(url, p, driverPath):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : str(p)}
    chromeOptions.add_experimental_option("prefs",prefs)
    chromedriver = str(driverPath)
    driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
    driver.get(url)
    elements = driver.find_elements_by_xpath("//a[contains(@href, '.mid')]")
    for x in range(0,len(elements)):
        if elements[x].is_displayed():
            elements[x].click()
    convertFiles(p, input("Enter full path to Midicsv: "))



def convertFiles(p, p1):
    arr_txt = [x for x in os.listdir(p) if x.endswith(".mid")]
    print(arr_txt)
    for x in arr_txt:
        batchPath = p + x[:-4]+".bat" 
        myBat = open(batchPath,'w+')
        writeLine = p1+" "+x+" "+x[:-4]+".csv"
        myBat.write(writeLine)
        myBat.close()

scrapeWebsite(input("Enter the URL of the website: "), input("Enter full path to storage location: "), input("Enter full path to ChromeDriver: "))
