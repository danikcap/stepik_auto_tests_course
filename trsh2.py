import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.execute_script("return alert('Hello!');")

finally:
    time.sleep(10)
    browser.quit()


