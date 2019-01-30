# This Script will test a PDP page and its regfom
# Example Ticket: WU-9830


from tkinter import Tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def exist_element(driver, classname):
    try:
        driver.find_element_by_class_name(classname)
        return True
    except:
        return False

def exist_header(driver, header):
    try:
        element = driver.find_element_by_css_selector("body > div.container-fluid > div:nth-child(2) > div > div > div > div > div > div > div > h1.headline").text
        if element == header:
            return True
        else:
            return False
    except:
        return False

def exist_feature_header(driver, text):
    try:
        element = driver.find_element_by_class_name("producthero--features-header").text
        if element == text:
            return True
        else:
            return False
    except:
        return False

def exist_subheader(driver, text):
    try:
        element = driver.find_element_by_class_name("producthero--subheader").text
        if element == text:
            return True
        else:
            return False
    except:
        return False

#Script configuration section - Change ir by the values that you need to#
coockieneeded = True # Change True if need to use cookies
subheader = "Gain the capability to quickly understand how configuration changes are impacting your network" #PDP Hero Subheader
features_header = "Combine the power of Network Performance Monitor (NPM) and Network Configuration Manager (NCM) so you can:" #PDP Key features header
reg_header = "Don't let device configuration errors impact your network performance." #Regform subheader


#Cookie definition
cookies = {
    "domain": ".solarwinds.com",
    "expirationDate": "1579980261",
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "CPDetails",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "{\"VisitorGUID\": \"77e3d2fd-5ed2-4f4c-ae51-4f5a603bd2f4\", \"Owned\" : [\"Orion NPM\",\"Orion SAM\"], \"Role\" : \"S\", \"Virtual Classroom Name\" : [\"Classroom name 1\",\"Classroom name 2\"],\"VR PMM Category\" : [\"Dameware\",\"Engineer\\'s Web Toolset\"]}",
    "id": "16"}
print(cookies)
# Cookie definition

urlList = Tk().clipboard_get().split('\n') #Get the URLs from the clipboard
print(urlList)
print("List Size:", len(urlList))
driver = webdriver.Chrome()
print(cookies)
for url in urlList:
    try:
        print(url)
        if coockieneeded: #Inserts the cookie
            driver.get('http://www.solarwinds.com')
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "logo-link"))
                )
            finally:
                driver.add_cookie(cookies)
                driver.get(url)
        else:
            driver.get(url)
        if exist_subheader(driver,subheader): #Search PDP Header
            print ("PDP Sub Header OK")
        else:
            print("PDP Sub Header not personalized")
        if exist_feature_header(driver, features_header): #Search for PDP feature header
            print("Feature Header Ok ")
        else:
            print("Missing Feature header")

        #Click on registration button
        element = driver.find_element_by_css_selector("body > div.container-fluid > div:nth-child(2) > div > div > div > div > div > div.row.producthero--table > div.col-xs-12.col-md-6.producthero--padding-right.producthero--table-cell-list > div:nth-child(3) > div > div > div > div:nth-child(1) > div:nth-child(1) > div > a:nth-child(1)")
        element.click()

        if exist_header(driver, reg_header):
            print("RegForm Header Ok")
        else:
            print("Missing Regform Header")
        if exist_element(driver, "wu-ul-bullets-list"):
            print("Regform bullets visible")
        else:
            print("Regform bullets not visible")
    finally:
        driver.delete_all_cookies()
driver.quit()