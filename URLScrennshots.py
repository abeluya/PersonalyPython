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
            #new_set = url.replace('https://', '').replace('/', '_')
            #print(new_set)
            #path = 'C:\\Users\\Abraham\\Documents\\Abraham\\Docs\\LEM\\' + new_set + '.png'
           # print(path)
            driver.get(url)
            #driver.find_element_by_tag_name('body')
            #driver.save_screenshot(path)

    except:
        print("Error")

driver.quit()