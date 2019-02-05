# This Script will test a PDP with the "Have an account" text under the download button in the CTA
# Example ticket: WU-9954

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

def exist_login(driver, header):
    try:
        element = driver.find_element_by_link_text("Log in to Download").text
        if element == header:
            return True
        else:
            return False
    except:
        return False


#Script configuration section - Change ir by the values that you need to#
coockieneeded = True # Change True if need to use cookies
button_text = "Log in to Download" #PDP Hero Subheader


#Cookie definition
cookies = {
    "domain": ".solarwinds.com",
    "expirationDate": "1580394557",
    "hostOnly": "false",
    "httpOnly": "false",
    "name": "CPDetails",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": "false",
    "session": "false",
    "storeId": "0",
    "value": "{\"VisitorGUID\": \"77e3d2fd-5ed2-4f4c-ae51-4f5a603bd2f4\", \"Owned\" : [\"DPA\",\"DPA for DB2\",\"DPA MySQL\",\"DPA Oracle\",\"DPA for SAP ASE\",\"DPA for SQL Server\",\"DPA VM Option\",\"NAT\",\"NCM\",\"NPM\",\"NTM\",\"Patch\",\"SAM\",\"SRM\",\"WPM\",\"DPA\",\"UDT\",\"Virtualization\",\"IPAM\",\"NTA\",\"Log Manager for Orion Software\",\"Database Performance Analyzer for Oracle\",\"Database Performance Analyzer for MySQL\",\"Log and Event Manager\",\"DPA SQL\"], \"Role\" : \"S\", \"Virtual Classroom Name\" : [\"Classroom name 1\",\"Classroom name 2\"],\"VR PMM Category\" : [\"Dameware\",\"Engineer's Web Toolset\"]}",
    "id": "4"}
print(cookies)
# Cookie definition

#Variables
urlList = Tk().clipboard_get().split('\n') #Get the URLs from the clipboard
all_ok = True
pages_to_check_list = []

#Variables end

print(urlList)
print("List Size:", len(urlList))
driver = webdriver.Chrome()
print(cookies)
if coockieneeded:  # Inserts the cookie
    driver.get('http://www.solarwinds.com')
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "logo-link"))
        )
    finally:
        driver.add_cookie(cookies)
for url in urlList:
    try:
        if url is not '':
            driver.get(url)
            error = False
            if exist_element(driver, "producthero--download-button-footer "):
                if exist_login(driver,button_text):
                    print(url, ": Have Account Visible")
                else:
                    print(url, ": Cannot find login button")
                    all_ok = False
                    error = True
            else:
                print(url, ": Have Account not visible")
                all_ok = False
                error = True
    finally:
        if error:
            pages_to_check_list.append(url)
driver.quit()

if all_ok:
    print("All pages are personalized")
else:
    print("Some pages are not personalized")
    for urls in pages_to_check_list:
        print(urls)


