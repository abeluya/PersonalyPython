# This Script will test a PDP with the "Have an account" text under the download button in the CTA
# This script will test every single synonim for its correspondig URL
# Example ticket: WU-9954

from tkinter import Tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Acronym:
    url = ""
    synonims = []


    def set_url(self, url):
        self.url = url

    def set_synonim(self, synonim):
        self.synonims.append(synonim)

    def set_synonims(self, synonims):
        self.synonims = synonims

    def get_url(self):
        return self.url

    def get_synonims(self):
        return self.synonims

    def get_synonim(self, index):
        return self.synonims[index]




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

def visible_lock(driver):
    try:
        element = driver.find_element_by_css_selector("body > div.container-fluid > div.container > div > div > div:nth-child(1) > div > div > div.row.producthero--table > div.col-xs-12.col-md-6.producthero--padding-right.producthero--table-cell-list > div:nth-child(3) > div > div > div > div > div:nth-child(2) > div > p > i")
        if element.is_displayed():
            return True
        else:
            return False
    except:
        return False


#Script configuration section - Change ir by the values that you need to#
coockieneeded = True # Change True if need to use cookies
button_text = "Log in to Download" #PDP Hero Subheader
hide_lock = True #Evaluates if the lock icon should be hiden

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
all_ok = True
pages_to_check_list = []

#Variables end

acronym_list = [Acronym()]
urlList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
for url in urlList:
    if len(url) >= 1:
        acronym = Acronym()
        test = url.split('\t')
        acronym.set_url(test[0])
        acronym.set_synonims(test[1].split(','))
        acronym_list.append(acronym)


print("List Size:", len(urlList))
driver = webdriver.Chrome()

if coockieneeded:  # Inserts the cookie
    driver.get('http://www.solarwinds.com')
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "logo-link"))
        )
    finally:
        print("site loaded")
try:
    for x in acronym_list:
        print(x.get_url())
        for y in x.get_synonims():
            value = "{\"VisitorGUID\": \"77e3d2fd-5ed2-4f4c-ae51-4f5a603bd2f4\", \"Owned\" : [\"" + y.strip() + "\"], \"Role\" : \"S\", \"Virtual Classroom Name\" : [\"Classroom name 1\",\"Classroom name 2\"],\"VR PMM Category\" : [\"Dameware\",\"Engineer's Web Toolset\"]}"
            cookie = {
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
                "value": value,
                "id": "4"}
            driver.add_cookie(cookie)
            driver.get(x.get_url())
            error = False
            if exist_element(driver, "producthero--download-button-footer "):
                if exist_login(driver,button_text):
                    print(y.strip(), ": Have Account Visible")
                    if hide_lock:
                        if not visible_lock(driver): #Check that lock icon is removed
                            print(y.strip(), ": Lock icon Hidden")
                        else:
                            print(y.strip(), ": Lock icon Visible")
                            all_ok = False
                            error = True
                else:
                    print(y.strip(), ": Cannot find login button")
                    all_ok = False
                    error = True
                    if hide_lock:
                        if not visible_lock(driver): #Check that lock icon is removed
                            print(y.strip(), ": Lock icon Hidden")
                        else:
                            print(y.strip(), ": Lock icon Visible")
                            all_ok = False
                            error = True
            else:
                print(y.strip(), ": Have Account not visible")
                all_ok = False
                error = True
            driver.delete_all_cookies()
            if error:
                if not x.get_url() in pages_to_check_list:
                    pages_to_check_list.append(x.get_url())
finally:
    driver.quit()

if all_ok:
    print("All pages are personalized")
else:
    print("Some pages are not personalized")
    for urls in pages_to_check_list:
        print(urls)


