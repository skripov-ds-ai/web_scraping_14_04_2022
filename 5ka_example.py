# pip install tqdm
# import time

# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://5ka.ru/special_offers"
DRIVER_PATH = "./selenium_drivers/chromedriver"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(DRIVER_PATH, options=options)
driver.get(URL)
# driver.refresh()
# //div[contains(@class, "product-card")]
# //button[@class='add-more-btn']
# more-btn-cont


def find_button(driver: webdriver.Chrome):
    return driver.find_element_by_class_name("more-btn-cont")


print()
# count = 0
# while True:
#     print()
#     time.sleep(3)
#     btn = find_button(driver)
#     btn.click()
#     print(f"Page number = {count}")
#     count += 1


# def find_button(driver):
#     return driver.find_element_by_class_name("add-more-btn")


i = 0
timeout = 10
while True:
    print(i)
    print()
    try:
        button = WebDriverWait(driver, timeout=timeout).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "more-btn-cont")
                # кнопка не кликабельна, но её "родитель" - да
                # EC.presence_of_element_located(
                #     (By.CLASS_NAME, "add-more-btn")
            )
        )
        print()
        button.click()
        i += 1
    except Exception as e:
        # please, write more special exceptions
        print(e)
        break
#
# time.sleep(30)
# driver.quit()


# i = 0
# while True:
#     print(i)
#     try:
#         button = find_button(driver)
#         button.click()
#         i += 1
#     except Exception as e:
#         # please, write more special exceptions
#         print(e)
#         break
