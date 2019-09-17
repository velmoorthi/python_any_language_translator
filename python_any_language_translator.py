from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 

From_language=input("Enter_from_language : ")
To_language=input("Enter to_language : ")
Input=input("Enter your text : ")

from_lang=From_language.lower()[:2]
to_lang=To_language.lower()[:2]


driver = webdriver.Chrome("/home/arun/Downloads/chromedriver") 
driver.get("https://translate.google.com/#view=home&op=translate&sl=%s&tl=%s"%(from_lang,to_lang)) 
print ("Opened google translator") 
time.sleep(1)

input1=driver.find_element_by_xpath('//*[@id="source"]')
input1.send_keys(Input)
time.sleep(2)

output=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div')
print("Your text in %s : "%To_language,output.text)

#driver.quit()

#"""
