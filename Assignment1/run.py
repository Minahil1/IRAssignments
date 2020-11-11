import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    count2=1
    while page <= max_pages:
        url = 'https://www.bbc.com/urdu/topics/cjgn7n9zzq7t/page/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'qa-heading-link lx-stream-post__header-link'}):
            all_data = []
            href = "https://www.bbc.com" + link.get('href')
            title = link.string
            # print(href)
            all_data.append(title)
            count = 1
            count2 =1
            get_single_item_data(href, all_data)
            for data in all_data:
                if count >= 1:
                    output = open('file' + str(count2) + '.txt', 'a', encoding='utf-8')
                    if data!=None:
                        output.write(data + "\r\n")
                    count += 1
                    output.close()
            count2+=1


def get_single_item_data(item_url, all_data):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('p'):
        all_data.append(item_name.string)


trade_spider(100)
