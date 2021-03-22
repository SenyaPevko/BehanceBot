
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from selenium.webdriver.common.by import By
url = ""
bot = "https://web.telegram.org/#/im?p=@behancer_bot"

# get browser's options that already have logged acounts
opts = Options()
opts.add_experimental_option("debuggerAddress", "localhost:9250")
driver = webdriver.Chrome(options=opts)


driver.get("https://web.telegram.org/#/im?p=@behancer_bot")


try:

    text = driver.find_element_by_class_name("composer_rich_textarea")
    driver.execute_script("arguments[0].send_keys();", text)
except Exception as ex:
    print(ex)
    sys.exit(1)
finally:
    print("yo")
