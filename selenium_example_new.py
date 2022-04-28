import os

# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
DRIVER_PATH = "./selenium_drivers/chromedriver"
