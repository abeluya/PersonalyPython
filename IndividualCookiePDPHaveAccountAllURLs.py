# This Script will test a PDP with the "Have an account" text under the download button in the CTA Using all given acronyms
# This script will test every single synonim for its correspondig URL
# Example ticket: WU-9954

from tkinter import Tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
    "secure": "False",
    "session": "False",
    "storeId": "0",
    "value": "{\"VisitorGUID\": \"77e3d2fd-5ed2-4f4c-ae51-4f5a603bd2f4\", \"Owned\" : [\"DPA\",\"DPA for DB2\","
             "\"DPA MySQL\",\"DPA Oracle\",\"DPA for SAP ASE\",\"DPA for SQL Server\",\"DPA VM Option\",\"NAT\","
             "\"NCM\",\"NPM\",\"NTM\",\"Patch\",\"SAM\",\"SRM\",\"WPM\",\"DPA\",\"UDT\",\"Virtualization\",\"IPAM\","
             "\"NTA\",\"Log Manager for Orion Software\",\"Database Performance Analyzer for Oracle\",\"Database "
             "Performance Analyzer for MySQL\",\"Log and Event Manager\",\"DPA SQL\"], \"Role\" : \"S\", "
             "\"Virtual Classroom Name\" : [\"Classroom name 1\",\"Classroom name 2\"],\"VR PMM Category\" : ["
             "\"Dameware\",\"Engineer's Web Toolset\"]}",
    "id": "4"}
print(cookies)
# Cookie definition

#Variables
all_ok = True
pages_to_check_list = []
acronym_list = [Acronym()]
synonyms_list = []

#Variables end

urlList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
for url in urlList:
    if len(url) > 0:
        acronym = Acronym()
        test = url.split('\t')
        if test[0] is not None:
            acronym.set_url(test[0])
            acronym.set_synonims(test[1].split(','))
            acronym_list.append(acronym)

for b in acronym_list:
    print(b.get_url())
    for y in b.get_synonims():
        if not y in synonyms_list:
            if y is not '':
                synonyms_list.append(y.strip())
print("Synonyms count:")
print(len(synonyms_list))
for b in synonyms_list:
    print(b)


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
        if x.get_url() is not '':
            print("URL: ", x.get_url(), "Valid Synonims: ", x.get_synonims())
            for y in synonyms_list:
                if y is not '':
                    value = "{\"VisitorGUID\": \"77e3d2fd-5ed2-4f4c-ae51-4f5a603bd2f4\", \"Owned\" : [\"" + y + "\"], \"Role\" : \"S\", \"Virtual Classroom Name\" : [\"Classroom name 1\",\"Classroom name 2\"],\"VR PMM Category\" : [\"Dameware\",\"Engineer's Web Toolset\"]}"
                    cookie = {
                        "domain": ".solarwinds.com",
                        "expirationDate": "1588536886",
                        "hostOnly": "false",
                        #"httpOnly": "false",
                        "name": "CPDetails",
                        "path": "/",
                        "sameSite": "no_restriction",
                        #"secure": "False",
                        "session": "False",
                        "storeId": "0",
                        "value": value,
                        "id": "4"}
                    driver.add_cookie(cookie)
                    driver.get(x.get_url())
                    error = False
                    if exist_element(driver, "producthero--download-button-footer"):
                        if exist_login(driver, button_text):
                            print(y.strip(), ": Have Account Visible")
                            if hide_lock:
                                if not visible_lock(driver): #Check that lock icon is removed
                                    print(y, ": Lock icon Hidden")
                                else:
                                    print(y, ": Lock icon Visible")
                                    all_ok = False
                                    error = True
                        else:
                            print(y.strip(), ": Cannot find login button")
                            all_ok = False
                            error = True
                            if hide_lock:
                                if not visible_lock(driver): #Check that lock icon is removed
                                    print(y, ": Lock icon Hidden")
                                else:
                                    print(y, ": Lock icon Visible")
                                    all_ok = False
                                    error = True
                    else:
                        print(y, ": Have Account not visible")
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
    for bad_urls in pages_to_check_list:
        print(bad_urls)


