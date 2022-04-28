import time

# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# pip install tqdm
from tqdm import trange

# from selenium.webdriver.common.keys import Keys


URL = "https://pikabu.ru/"
DRIVER_PATH = "./selenium_drivers/chromedriver"
MAX_PAGE_NUMBER = 5

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(DRIVER_PATH, options=options)

driver.get(URL)

html = ""

for i in trange(MAX_PAGE_NUMBER):
    time.sleep(5)
    articles = driver.find_elements_by_tag_name("article")
    if not articles:
        break
    actions = ActionChains(driver)
    actions.move_to_element(articles[-1])
    # Ctrl + C
    # actions.key_down(Keys.CONTROL).key_down("C")
    # actions.key_up(Keys.CONTROL).key_up("C")
    # Keys.END - maybe good for infinite feed
    # actions.send_keys(Keys.END)

    actions.perform()
    # в случае если нет исключений
    html = driver.page_source
# html-код страницы на данный момент
# driver.page_source
print()
