import requests
from bs4 import BeautifulSoup
import csv

request = requests.get(url="https://books.toscrape.com/")
page_source = request.content
soup = BeautifulSoup(page_source, "html.parser")

heading_elem = soup.find_all("h3")
price = soup.find_all("p", {"class": "price_color"})

complete_data = []

for each_heading, each_price in zip(heading_elem, price):
    each_link = each_heading.find("a")
    book_name = each_link.get("title")
    link = each_link.get("href")
    book_price = each_price.get_text()

    complete_data.append({
        "book_name": book_name,
        "book_price": book_price,
        "book_link": link
    })

filename = "book_data.csv"
fields_name = ["book_name", "book_price", "book_link"]

with open(filename, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields_name)
    writer.writeheader()
    for book_data in complete_data:
        writer.writerow(book_data)
