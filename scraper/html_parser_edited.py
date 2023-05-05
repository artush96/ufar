import sys
import requests
from bs4 import BeautifulSoup


class Scraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    categories = {
        "Real Estate": 54,
        "Vehicles": 16,
        "Electronics": 4,
        "Appliances": 26,
        "Home and Garden": 133,
        "Clothing and Fashion": 17,
        "Baby and Kids": 27,
        "Hobbies and Sports": 39,
        "Equipment and Materials": 84,
        "Pets and Animals": 37,
        "Food and Beverages": 14,
        "Services": 65,
        "Jobs": 29
    }
    locations = {
        "Yerevan": "?n=1&price1=&price2=&crc=-1", "Armavir": "?n=23&price1=&price2=&crc=-1",
        "Ararat": "?n=19&price1=&price2=&crc=-1", "Kotayk": "?n=40&price1=&price2=&crc=-1",
        "Shirak": "?n=49&price1=&price2=&crc=-1", "Lorri": "?n=44&price1=&price2=&crc=-1",
        "Gegharkunik": "?n=35&price1=&price2=&crc=-1", "Syunik": "?n=52&price1=&price2=&crc=-1",
        "Aragatsotn": "?n=14&price1=&price2=&crc=-1", "Tavush": "?n=57&price1=&price2=&crc=-1",
        "Vayots Dzor": "?n=61&price1=&price2=&crc=-1", "Artsakh": "?n=27&price1=&price2=&crc=-1",
        "International": "?n=116&price1=&price2=&crc=-1"
    }

    def __init__(self):
        self.domain = "https://www.list.am/"

        for cats in self.categories:
            print('○' + cats)
        key = input("Choose a category from above: ")
        if input("Do you want to specify the location? ").lower() == "yes":
            for locs in self.locations:
                print('➡' + locs)
            location = input("Choose the location from above: ").lower().capitalize()
            if input("Do you want to specify the price range? ").lower() == "yes":
                min_price = str(input("Enter the starting price: "))
                max_price = str(input("Enter the final price: "))
                url = self.price_setter(min_price, max_price, key)
            else:
                url = self.search_category(key) + self.find_location(location)
        else:
            url = self.search_category(key)
            if input("Do you want to specify the price range? ").lower() == "yes":
                min_price = input("Enter the starting price: ")
                max_price = input("Enter the final price: ")
                url = url + f"?n=0&price1={min_price}&price2={max_price}&crc=-1"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            class_name = "dl"
            c_div = soup.find('div', {'id': 'contentr'})
            div = c_div.find('div', {'class': 'dl'})
            if div:
                links = div.find_all('a')
                for link in links:
                    print('•' + link.text)
            else:
                print(f"Error: 'div' element with class name {class_name} not found")
                sys.exit()
        else:
            print(f"Error: Could not retrieve webpage, status code {response.status_code}")
            sys.exit()

    def find_id(self, key):
        if self.categories.get(key):
            return self.categories[key]
        else:
            print(f"'{key}' does not exist")
            sys.exit()

    def find_location(self, location):
        if self.locations.get(location):
            return self.locations[location]
        else:
            print(f"'{location}' does not exist")
            sys.exit()

    def search_category(self, key):
        id1 = self.find_id(key)
        url = f"{self.domain}en/category/{id1}"
        return url

    def price_setter(self, min_price, max_price, key):
        id1 = self.find_id(key)
        price = f"{self.domain}en/category/?n={id1}&price1={min_price}&price2={max_price}&crc=-1"
        return price
