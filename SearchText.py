from tkinter import Tk
from selenium import webdriver

# Methods definition
def exist_element(driver, classname):
    try:
        e = driver.find_element_by_class_name(classname)
        return e
    except:
        return False

def exist_header(driver, header):
    try:
        element = driver.find_element_by_class_name("topic-backlink-container").text
        if element == header:
            return element
        else:
            return element
    except:
        return False

def get_url(driver, classname):
    try:
        e = driver.find_element_by_class_name(classname)
        print(e.get_attribute("href"))
        return e.get_attribute("href")
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
            #element = driver.page_source.find("« View all Server & Application Monitor use cases")
            #element = driver.find_elements_by_xpath("//*[contains(text(), '« View all Server & Application Monitor use cases')]")
            # element = exist_element(driver, "topic-backlink-container")
            #if element.text == "« View all Log & Event Manager use cases":
                #element = get_url(driver, "topic-backlink-container")
                #if element == "https://author.azure.solarwinds.com/log-event-manager-software/use-cases":
                    #print(url + " OK")
            #else:
                #print(url + " ERROR")
    except:
        print("Error")

driver.quit()