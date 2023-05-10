import requests
from bs4 import BeautifulSoup


class Scraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    categories = {
        "Real Estate": 54,
        "Transport": 16,
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
        "Yerevan": "1", "Armavir": "23",
        "Ararat": "19", "Kotayk": "40",
        "Shirak": "49", "Lorri": "44",
        "Gegharkunik": "35", "Syunik": "52",
        "Aragatsotn": "14", "Tavush": "57",
        "Vayots Dzor": "61", "Artsakh": "27",
        "International": "116"
    }

    def __init__(self):
        self.domain = "https://www.list.am/"
        self.data = []

    def parse(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            class_name = "dl"
            c_div = soup.find('div', {'id': 'contentr'})
            div = c_div.find('div', {'class': 'dl'})
            if div:
                links = div.find_all('a')
                for link in links:
                    self.data.append(link.text)
        return self.data

    def find_id(self, key):
        if self.categories.get(key):
            return self.categories[key]

    def query(self, query):
        url = self.get_url(query)
        print(url)
        data = self.parse(url)
        return data

    @staticmethod
    def get_location(query):
        location_path = f'?n={Scraper().locations.get(query.get("location"))}'
        return location_path

    @staticmethod
    def get_category(query):
        cat_path = f'category/{Scraper().categories.get(query.get("category"))}'
        return cat_path

    @staticmethod
    def get_min_price(query):
        min_price_path = f'&price1={query.get("min_price")}'
        return min_price_path

    @staticmethod
    def get_max_price(query):
        max_price_path = f'&price2={query.get("max_price")}'
        return max_price_path

    def get_url(self, query):
        url = f'{self.domain}{self.get_category(query)}{self.get_location(query)}' \
              f'{self.get_min_price(query)}{self.get_max_price(query)}&crc=-1'
        return url
