import requests
from bs4 import BeautifulSoup

url = 'https://www.list.am/am/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    for i in range(1, 20):
        class_name = f"c c{i}"
        c_div = soup.find('div', {'class': class_name})
        if c_div:
            links = c_div.find_all('a')
            for link in links:
                print(link.text)
            break
    else:
        print("Error: 'div' element not found")
else:
    print(f"Error: Could not retrieve webpage, status code {response.status_code}")
