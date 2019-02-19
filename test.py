

from tkinter import Tk
from selenium import webdriver


def exist_login(driver, header):
    try:
        element = driver.find_element_by_link_text("Log in to Download").text
        if element == header:
            return True
        else:
            return False
    except:
        return False

# variables
urlList = Tk().clipboard_get().split('\n')  # Get the URLs from the clipboard
all_ok = True
pages_to_check_list = []
# variables end

print("List Size:", len(urlList))
print(urlList)

