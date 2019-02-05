# This Script will test a list of URLs that has CMP codes (Only for regforms)
# Example Ticket: WU-9814


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


#Script configuration section
reg_header = "Due diligence means deeper visibility" #Change it by the header you want to find


#Script configuration section end

#variables
urlList = Tk().clipboard_get().split('\n') #Get the URLs from the clipboard
all_ok = True
pages_to_check_list = []
#variables end

print(urlList)
print("List Size:", len(urlList))
driver = webdriver.Chrome()
for url in urlList:
    try:
        if len(url) > 0:
            print(url)
            error = False
            driver.get(url)
            if exist_header(driver, reg_header):
                print("RegForm Header Ok")
            else:
                print("Missing Regform Header")
                all_ok = False
                error = True
            if exist_element(driver, "wu-ul-bullets-list"):
                print("Regform bullets visible")
            else:
                print("Regform bullets not visible")
                all_ok = False
                error = True
    finally:
        if error:
            pages_to_check_list.append(url)
        driver.delete_all_cookies()

driver.quit()
if all_ok:
    print("All pages are personalized")
else:
    print("Some pages are not personalized")
    for urls in pages_to_check_list:
        print(urls)