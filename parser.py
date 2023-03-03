import requests
from bs4 import BeautifulSoup

from config import login, password

session = requests.Session()

auth_res = session.post("https://klasnaocinka.com.ua/uk/user/user/login", data={"LoginForm[login]":login, "LoginForm[password]": password})

if auth_res.status_code == 200:
    print("Auth successful")

res = session.get("https://klasnaocinka.com.ua/diary/diary/index")

soup = BeautifulSoup(res.text, "html.parser")

days = soup.findAll('table', class_='day_lesson_long')

for d in days:
    print(d)

