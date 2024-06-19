import requests
from bs4 import BeautifulSoup
import csv

def scrape_flipkart_data():
    Product_names = []
    Prices = []
    Descriptions = []
    Reviews = []

    for page_num in range(1, 5):
        url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=2&as-type=HISTORY&page=" + str(page_num)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="KzDlHZ")
        for i in names:
            name = i.text
            Product_names.append(name)

        prices = soup.find_all("div", class_="Nx9bqj _4b5DiR") 
        for i in prices:
            price = i.text
            Prices.append(price)

        descriptions = soup.find_all("ul", class_="G4BRas")
        for i in descriptions:
            description = i.text
            Descriptions.append(description)

        reviews = soup.find_all("div", class_="XQDdHH")
        for i in reviews:
            review = i.text
            Reviews.append(review)

    return Product_names, Prices, Descriptions, Reviews

def write_to_csv(product_names, prices, descriptions, reviews):
    with open("flipkart_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Product Name", "Price", "Description", "Review"])
        for data in zip(product_names, prices, descriptions, reviews):
            writer.writerow(data)

if __name__ == "__main__":
    product_names, prices, descriptions, reviews = scrape_flipkart_data()
    write_to_csv(product_names, prices, descriptions, reviews)
    print("Data has been written to flipkart_data.csv")
