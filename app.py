import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
questions = soup.select(".s-post-summary--content-title")

for question in questions:
    print(question.select_one(".s-link").getText())
