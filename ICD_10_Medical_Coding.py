
import icd10
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Cholera = {"A00": "Cholera", "A00.0": "Cholera due to Vibrio cholerae 01, biovar cholerae Classical cholera",
#            "A00.1": "Cholera due to Vibrio cholerae 01, biovar eltor Cholera eltor", "A00.9": "Cholera, unspecified"}

#Typhoid = {"A01": "Typhoid and paratyphoid fevers", "A01.0": "Typhoid fever, Infection due to Salmonella typhi",
#            "A01.1": "Paratyphoid fever A", "A01.2": "Paratyphoid fever B", "A01.3": "Paratyphoid fever C", 
#            "A01.4": "Paratyphoid fever, unspecified, Infection due to Salmonella paratyphi NOS"}

#Salmonella = {"A02": "Other - infection or foodborne intoxication due to any Salmonella species other than S. typhi and S. paratyphi",
#                "A02.0": "Salmonella enteritis, Salmonellosis", "A02.1": "Salmonella sepsis", "A02.2": "Localized salmonella infections",
#                "A02.8": "Other specified salmonella infections", "A02.9": "Salmonella infection, unspecified"}

#Shigellosis = {"A03": "Shigellosis", "A03.0": "Shigellosis due to Shigella dysenteriae -Group A", "A03.1": "Shigellosis due to Shigella flexneri -Group B",
#                "A03,2": "Shigellosis due to Shigella boydii -Group C", "A03.3": "Shigellosis due to Shigella sonnei -Group D", "A03.8": "Other shigellosis",
#                "A03.9": "Shigellosis, unspecified, Bacillary dysentery NOS"}

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

    