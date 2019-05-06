from tkinter import Tk
from selenium import webdriver

# Methods definition
def exist_element(driver, classname):
    try:
        driver.find_element_by_class_name(classname)
        return True
    except:
        return False

def exist_header(driver, header):
    try:
        element = driver.find_element_by_class_name("headline").text
        if element == header:
            return True
        else:
            return False
    except:
        return False



# Methods definition end


class URLs:
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

driver = webdriver.Chrome()
urlList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
print(len(urlList))
print(urlList)
for url in urlList:
    print(url)

for url in urlList:
    try:
        if url is not '':
            driver.get(url)
            error = False
            priceValue = driver.find_element_by_xpath("/html/head/meta[5]")
            if priceValue.get_attribute("content") == "noindex, nofollow":
                print(url + " OK")
            else:
                print(url + "ERROR")
    except:
        print("Error")

driver.quit()