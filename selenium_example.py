import os
import time

# pip install python-dotenv
from dotenv import load_dotenv

# pip install selenium
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

# from urllib.parse import urljoin


load_dotenv()


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
DRIVER_PATH = "./selenium_drivers/chromedriver"
# For Windows
# DRIVER_PATH = "./selenium_drivers/chromedriver.exe"

url = "https://gb.ru/login"

# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options)

options = webdriver.ChromeOptions()
# options.add_argument("--window-size=200,200")
options.add_argument("--start-maximized")


driver = webdriver.Chrome(DRIVER_PATH, options=options)
driver.get(url)

# email_field = driver.find_element_by_name("user[email]")
# email_field.clear()
# email_field.send_keys(EMAIL)
#
# password_field = driver.find_element_by_id("user_password")
# # имитация ввода + ENTER
# # password_field.send_keys(PASSWORD + "\n")
# # password_field.send_keys(PASSWORD + Keys.ENTER)
# password_field.send_keys(PASSWORD)
# password_field.send_keys(Keys.ENTER)
#
# time.sleep(5)
#
# url_for_edit = "https://gb.ru/profile?tab=info"
# driver.get(url_for_edit)
#
# time.sleep(2)
#
# patronymic = driver.find_element_by_name("user[middle_name]")
# patronymic.send_keys("Сергеевич")
#
# gender = driver.find_element_by_name("user[gender]")
# select = Select(gender)
# select.select_by_value("male")
#
# gender.submit()
# # patronymic.submit()
#
# # time.sleep(7)
# #
# # select.select_by_visible_text("Не выбран")
#
# url_for_logout = "https://gb.ru/logout"
# driver.get(url_for_logout)

time.sleep(3)

# закрывает текущую вкладку
# driver.close()

# закрывает браузер
driver.quit()


# email_field = driver.find_element_by_name("user[email]")
# email_field.send_keys(EMAIL)
#
# password_field = driver.find_element_by_id("user_password")
# password_field.send_keys(PASSWORD + "\n")
# # password_field.send_keys(PASSWORD + Keys.ENTER)
# # password_field.send_keys(PASSWORD)
# # password_field.send_keys(Keys.ENTER)
#
# # Предположим использование get_attribute("href")
# # new_url = urljoin(url, url_by_href)
# new_url = "https://gb.ru/profile?tab=info"
#
# driver.get(new_url)
# city_field = driver.find_element_by_name("user[city]")
# # Очищаем поле от данных
# city_field.clear()
# # Город не сохранился т.к. происходит
# # валидация города перед сохранением,
# # отправкой на сервер
# city_field.send_keys("Ufa")
# # Очищаем поле от данных
# city_field.clear()
#
# time.sleep(2)
#
# gender = driver.find_element_by_name("user[gender]")
# select = Select(gender)
# select.select_by_value("unknown")
# gender.submit()
#
# time.sleep(2)


# url = "https://gb.ru/logout"
# driver.get(url)
# time.sleep(9)

# закрывает активную вкладку
# driver.close()
# закрывает браузер целиком
# driver.quit()


# user_mail = driver.find_element_by_id("user_email")
# user_mail.send_keys(EMAIL)
#
# user_password = driver.find_element_by_id("user_password")
# user_password.send_keys(PASSWORD)
# # user_password.send_keys(PASSWORD + "\n")
# # user_password.send_keys("\n")
# user_password.send_keys(Keys.ENTER)
# # time.sleep(10)
#
# url = "https://gb.ru/profile"
# driver.get(url)
# # time.sleep(5)
# city = driver.find_element_by_name("user[city]")
# # TODO: fix clearing
# city.send_keys("")
# city.clear()
# # time.sleep(2)
# city.send_keys("Рим")
#
# gender = driver.find_element_by_name("user[gender]")
# select = Select(gender)
# # unknown
# # select.select_by_index(0)
# # time.sleep(2)
# select.select_by_value("female")
# # time.sleep(7)
# select.select_by_visible_text("Не выбран")
# gender.submit()
#
#
# time.sleep(9)
# url = "https://gb.ru/logout"
# driver.get(url)
#
# # time.sleep(20)
# # close browser?
# # driver.close()
# driver.quit()
