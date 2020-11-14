import requests
from bs4 import BeautifulSoup


def get_html(url):
    result = requests.get(url)
    return result.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    rooms = soup.find_all('a', class_ = 'room')
    r = []
    for item in rooms:
        metro = item.find('div', class_="room-footer").find('span')
        address = item.find('div', class_="room-footer").text.split(metro.text if metro else ' ')
        address = address[1].replace("\n", "").replace(" ", "") if len(address) > 1 else "N/A"
        r.append({
            'room_name' : item.find('div', class_ = 'room-name').find('div').text,
            'link' : item.get('href'),
            'address' : f"{metro.text if metro else 'N/A'}, {address}"
        })
    return r
    

def main(url):
    html = get_html(url)
    return get_data(html)

print("Hui")

url = 'https://kadroom.com'

print(main(url))
