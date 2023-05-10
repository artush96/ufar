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


def scrapper_run(self):
    key = self.get_category
    if self.get_location != None:
        location = self.get_location
        if self.get_min_price() != None:
            min_price = self.get_min_price
            max_price = self.get_max_price
            url = self.get_url(min_price, max_price, key)
        else:
            url = self.get_category(key) + self.get_location(location)
    else:
        url = self.get_url(key)
        min_price = self.get_min_price
        max_price = self.get_max_price
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
                self.data.append(link.text)


def find_id(self, key):
    if self.categories.get(key):
        return self.categories[key]


def query(self, query):
    url = self.get_url(query)

    req = self.request(url)
    data = self.parse(req)
    return data


@staticmethod
def get_location(query):
    location_path = f'?n={query.get("location")}'
    return location_path


@staticmethod
def get_category(query):
    cat_path = f'category/{query.get("category")}'
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
    url = f'{self.domain}/en/{self.get_category(query)}/{self.get_location(query)}' \
          f'{self.get_min_price(query)}{self.get_max_price(query)}&crc=-1'
    return url
