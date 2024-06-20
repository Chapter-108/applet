# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def fetch_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('title').text if soup.find('title') else 'No Title'
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return title, links


def main():
    url = input("爬取的网站: ")
    html = fetch_page(url)
    if html:
        title, links = parse_page(html)
        try:
            print(f"Page Title: {title}")
        except UnicodeEncodeError:
            print(f"Page Title: {title.encode('utf-8', 'ignore').decode('utf-8', 'ignore')}")

        print("Links found:")
        for link in links:
            try:
                print(link)
            except UnicodeEncodeError:
                print(link.encode('utf-8', 'ignore').decode('utf-8', 'ignore'))
    else:
        print("Failed to retrieve the webpage.")


if __name__ == "__main__":
    main()
