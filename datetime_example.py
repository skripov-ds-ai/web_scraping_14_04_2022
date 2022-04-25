from datetime import datetime

now = datetime.now()
print(now)
print(type(now))
print(now.date())
print(str(now.date()))
example_news_time = datetime.fromtimestamp(1618594868005166830 / 10**9)
print(example_news_time)
