
import icd10
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Using PathGroup.com for providing the Most Common Family Practice Diagnostics used in Healthcare.

Data = {"Z00.00": " Encntr for general adult medical exam w/o abnormal findings", "Z12.4": "Encounter for screening for malignant neoplasm of cervix",
"I10": "Essential (primary) hypertension", "Z12.5": "Encounter for screening for malignant neoplasm of prostate", "E11.9": "Type 2 diabetes mellitus without complications",
"G93.3": "Postviral fatigue syndrome", "R53.1": "Weakness", "R53.81": "Other malaise", "R53.83": "Other fatigue", "N39.0": "Urinary tract infection, site not specified",
"E78.4": "Other hyperlipidemia", "E78.5": "Hyperlipidemia, unspecified", "Z00.00": "Encntr for general adult medical exam w/o abnormal findings", "E03.9": "Hypothyroidism, unspecified",
"Z79.891": "Long term (current) use of opiate analgesic", "Z79.899": "Other long term (current) drug therapy", "R30.0": "Dysuria", "R30.9": "Painful micturition, unspecified", "E78.2": "Mixed hyperlipidemia",
"E78.0": "Pure hypercholesterolemia", "E55.9": "Vitamin D deficiency, unspecified", "J02.9": "Acute pharyngitis, unspecified", "E11.65": "Type 2 diabetes mellitus with hyperglycemia", "Z79.01": "Long term (current) use of anticoagulants",
"R10.9": "Unspecified abdominal pain", "D64.9": "Anemia, unspecified", "I48.91": "Unspecified atrial fibrillation", "R31.9": "Hematuria, unspecified", "K52.2": "Allergic and dietetic gastroenteritis and colitis",
"K52.89": "Other specified noninfective gastroenteritis and colitis", "R19.7": "Diarrhea, unspecified", "R50.2": "Drug induced fever", "R50.9": "Fever, unspecified", "Z72.51": "High risk heterosexual behavior", "Z00.00": "Encntr for general adult medical exam w/o abnormal findings",
"R78.89": "Finding of oth substances, not normally found in blood", "R79.0": "Abnormal level of blood mineral", "R79.89": "Other specified abnormal findings of blood chemistry", "N30.00": "Acute cystitis without hematuria", "N30.01": "Acute cystitis with hematuria", "E29.1": "Testicular hypofunction",
"E01.8": "Oth iodinedeficiency related thyroid disord and allied cond", "E03.8": "Other specified hypothyroidism", "N76.0": "Acute vaginitis", "N76.1": "Subacute and chronic vaginitis", "N76.2": "Acute vulvitis", "N76.3": "Subacute and chronic vulvitis", "Z00.129": "Encntr for routine child health exam w/o abnormal findings",
"R05": "Cough", "R73.09": "Other abnormal glucose", "K21.9": "Gastroesophageal reflux disease without esophagitis", "Z11.8": "Encounter for screening for oth infec/parastc diseases", "R60.0": "Localized edema", "R60.1": "Generalized edema", "R60.9": "Edema, unspecified", "Z13.220": "Encounter for screening for lipoid disorders",
"R42": "Dizziness and giddiness", "Z01.411": "Encntr for gyn exam (general) (routine) w abnormal findings", "Z01.419": "Encntr for gyn exam (general) (routine) w/o abn findings", "Z34.80": "Encounter for suprvsn of normal pregnancy, unsp trimester", "Z34.90": "Encntr for suprvsn of normal pregnancy, unsp, unsp trimester",
"D50.9": "Iron deficiency anemia, unspecified", "F41.9": "Anxiety disorder, unspecified", "L03.90": "Cellulitis, unspecified", "L03.91": "Acute lymphangitis, unspecified", "R10.84": "Generalized abdominal pain", "M25.50": "Pain in unspecified joint", "R35.0 ": "Frequency of micturition", "G44.1": "Vascular headache, not elsewhere classified",
"R51": "Headache", "R63.5": "Abnormal weight gain", "E11.40": "Type 2 diabetes mellitus with diabetic neuropathy, unsp", "J44.9": "Chronic obstructive pulmonary disease, unspecified", "I50.9": "Heart failure, unspecified", "R31.9": "Hematuria, unspecified", "R73.09": "Other abnormal glucose", "M12.9": "Arthropathy, unspecified", "E87.6": "Hypokalemia",
"J02.9": "Acute pharyngitis, unspecified", "E11.29": "Type 2 diabetes mellitus w oth diabetic kidney complication", "E01.2": "Iodinedeficiency related (endemic) goiter, unspecified", "E04.9": "Nontoxic goiter, unspecified"}

while True:
    print("Select 1 for Code Description, 2 to find Code by description, 3 to update Database or 0 to exit")
    Press = int(input())
    for Choice in range(1):
        
        if Press == 0:
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
            for key, value in Data.items():
                if Description in value:
                    print(key)

                    code = icd10.find(key)
                    if code.billable:
                        print(code, "is billable")
                    else:
                        print(code, "is not billable")
            else:
                print("Keyphrase is not found in local Database: Press 1 for results from Web or 2 for Main Menu.")
                Choice = int(input())
                if Choice == 1:

                    web = webdriver.Chrome()
                    web.get("https://icd.who.int/browse10/2019/en") #browser containing all updated ICD-10 Codes with Description.
                    
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
                elif Choice == 2:
                    break
                
                else:
                    print("Selection Does Not Exist")

        if Press == 3:
            print("Enter ICD-10 Code: include decimal points if any")
            ICD_10_Code = str(input())
            print("Enter Description: Ensure to insert accurate ICD-10 Guideline Description")
            ICD_10_Description = str(input())
            Data.update({ICD_10_Code : ICD_10_Description})
            print(list(Data)[-1])
            print("Database Updated")


            
