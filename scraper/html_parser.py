from requests import Session

from config import URL


class Scraper:
    headers = {

    }

    def __init__(self):
        self.session = Session()
        
