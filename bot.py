# chrome.exe --remote-debugging-port=9250 --user-data-dir="C:\chromedriver"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import re
import sys

url = ""
bot = "https://web.telegram.org/#/im?p=@behancer_bot"
to_do = "Like"

# get browser's options that already have logged acounts
opts = Options()
opts.add_experimental_option("debuggerAddress", "localhost:9250")
driver = webdriver.Chrome(options=opts)

# open telegram bot
driver.get(url=bot)

while True:
    try:

        time.sleep(2)

        # finding the url
        for message in driver.find_elements_by_class_name("im_message_text"):
            if "https" in message.text:
                # get the url from the message
                pattern = r'((?:#|http)\S+)'
                project_url = re.findall(pattern, message.text)
                url = project_url[0]
                if "лайк" in message.text:
                    to_do = "Like"
                elif "комментарий" in message.text:
                    to_do = "Comment"

        # open behance
        time.sleep(2)
        driver.get(url=url)

        # send comment or like
        if to_do == "Like":
            # like on behance
            for button in driver.find_elements_by_class_name("Project-actionName-1sX"):
                if button.text == "Оценить":
                    driver.execute_script("arguments[0].click();", button)
                elif button.text == "Оценено":
                    driver.execute_script("arguments[0].click();", button)
                    driver.execute_script("arguments[0].click();", button)
        else:
            # comment on behance
            commentArea = driver.find_element_by_id("comment")
            commentArea.send_keys("Awesome work, dude")
            button = driver.find_elements(By.XPATH, '//a')
            for a in button:
                if a.text == "Опубликовать комментарий":
                    driver.execute_script("arguments[0].click();", a)

        # open telegram bot
        driver.get(url=bot)
        time.sleep(2)

        # click on button that you've liked the post
        button = driver.find_elements(By.XPATH, '//button')
        for a in button:
            if "Готово" in a.text:
                a.click()
        time.sleep(4)
        driver.refresh()

    except Exception as ex:
        print(ex)
        sys.exit(1)
    finally:
        print("yo")
