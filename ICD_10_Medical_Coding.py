
import icd10
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

while True:
    print("Select 1 to find Code Description, 2 to find Code by description or 3 to exit")
    Press = int(input())
    for Choice in range(1):
        
        if Press == 3:
            sys.exit()

        if Press == 1:
            print("Enter Single Alphabet: A - Z")

            Alphabet = str(input())

            print("Find Description By Entering the 2 digit Number including decimal points if any")

            Digit = input()

            code = icd10.find(Alphabet + str(Digit))
            print(code.description)
            if code.billable:
                print(code, "is billable")
            else:
                print(code, "is not billable")

        if Press == 2:
            print("Enter Key Phrase/ Description: EG - Cholera")

            Description = str(input())

            web = webdriver.Chrome()
            web.get("https://icd.who.int/browse10/2019/en")
            
            time.sleep(1)
                    
            Search = web.find_element_by_xpath('//*[@id="advancedSearchButton"]')
            Search.click()

            time.sleep(1)

            Search1 = web.find_element_by_xpath('//*[@id="Search_Definition"]')
            Search1.click()

            time.sleep(1)

            SearchIndex = Description
            insert = web.find_element_by_xpath('//*[@id="SearchText"]')
            insert.send_keys(SearchIndex)

            submitButton = web.find_element_by_xpath('/html/body/div[8]/div[3]/div/button/span')
            submitButton.click()

            Close = web.find_element_by_xpath('/html/body/div[8]/div[1]/button/span[1]')
            Close.click()

    
