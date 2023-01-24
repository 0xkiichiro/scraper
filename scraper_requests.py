from bs4 import BeautifulSoup
import requests

scraped_data = []
page = 1
url = f"https://www.trendyol.com/sr?wg=1%2C2&cid=604351%2C617606&pi1=&pi={page}"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
total_items = int(soup.find('div', class_='dscrptn').text.split(' ')[0])

while len(scraped_data) + 1 <= total_items:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.find_all("div", class_="p-card-wrppr with-campaign-view")
    page_item_counter = 0

    for item in items:
        if "{item}" not in scraped_data:
            scraped_data.append(f"{item}")
            page_item_counter += 1
            print('array length: ', len(scraped_data))
        if page_item_counter >= len(items):
            page += 1
            url = f"https://www.trendyol.com/sr?wg=1%2C2&cid=604351%2C617606&pi1=&pi={page}"
            print('on page: ', page)

with open("./scrape.txt", "w") as outfile:
            list_stringfy = ""
            for item in scraped_data:
                list_stringfy += str(item) + "\n"
            outfile.write(list_stringfy)