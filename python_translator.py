from selenium import webdriver # install using pip (pip install selenium)
from selenium.webdriver.common.keys import Keys 
import time 

while True:
    From_language=input("Enter_from_language : ")    #translate from
    To_language=input("Enter to_language : ")  #translate into

    Input=input("Enter your text : ")  # input text

    from_lang=From_language.lower()[:2]  #to pass language to the url
    to_lang=To_language.lower()[:2]


    driver = webdriver.Chrome("D:/velu/datascience/python_mini_projects/chromedriver")  #location of your chrome driver exe
    # download from this link 'https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.138/'

    # google translator url
    driver.get("https://translate.google.com/#view=home&op=translate&sl=%s&tl=%s"%(from_lang,to_lang)) # pass from lang and to lang to the url
    time.sleep(1)

    input1=driver.find_element_by_xpath('//*[@id="source"]')  # input area of google translator
    input1.send_keys(Input)
    time.sleep(2)

    # output area of google translator
    output = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span') 
    print("Your text in %s : "%To_language,output.text)

    #driver.quit() # to close the browser

    key = input('Press c to continue or press any key to quit : ')

    if key != 'c':
        break
        
