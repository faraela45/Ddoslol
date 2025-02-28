import requests
from bs4 import BeautifulSoup

def download_proxies(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    proxies = []

    for row in soup.find('table', {'id': 'proxylisttable'}).find_all('tr')[1:]:
        cols = row.find_all('td')
        ip = cols[0].text
        port = cols[1].text
        proxies.append(f'{ip}:{port}')

    with open(output_file, 'w') as f:
        for proxy in proxies:
            f.write(proxy + '\n')

if __name__ == "__main__":
    url = 'https://www.free-proxy-list.net/'
    output_file = 'proxies.txt'
    download_proxies(url, output_file)