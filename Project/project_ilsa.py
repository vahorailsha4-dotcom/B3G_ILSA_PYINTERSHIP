import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")
all_books = soup.find_all("article", class_="product_pod")
books_data = []

for book in all_books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]
    book_info = {
        "title": title,
        "price": price,
        "rating": f"{rating} stars"
    }
    books_data.append(book_info)

with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
    header = ["title", "price", "rating"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(books_data)

    print("Scraping completed! Check for books.csv file in the file list.")