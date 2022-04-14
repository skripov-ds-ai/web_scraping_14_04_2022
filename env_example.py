# good to know: pathlib, glob
import os

from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv("./.env")

key = "NAME"
result1 = os.environ[key]
# for example
result2 = os.environ.get(key, default=42)
result3 = os.getenv(key)

print()

print("42")
print()

# key = "USER_NAME"
# user_name = os.getenv(key, None)
# user_name1 = os.environ.get(key, None)
# workbook = os.getenv("WORKBOOK", 0)
# # what about types?
# wrong_workbook = os.getenv("WRONG_WORKBOOK", 0)
#
# print(user_name)
# print(user_name1)
# print(workbook)
# print(wrong_workbook)
# print()
