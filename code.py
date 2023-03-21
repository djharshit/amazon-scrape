import requests
from bs4 import BeautifulSoup
import faker
import csv

csvfile = open(file='web\\amazon\\res.csv', mode='w', newline='')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['name', 'url', 'price', 'rating'])

site = 'https://www.amazon.in/s'
head = {
    'User-Agent': faker.Faker().chrome()
}
query = {
    'k': 'bags',
    'crid': '2M096C61O4MLT',
    'qid': '1653308124',
    'prefix': 'ba,aps,283',
    'ref': 'sr_pg_1',
    'page': 1
}

for i in range(1, 11):
    query['page'] = i
    response = requests.get(url=site, headers=head, params=query)

    soup = BeautifulSoup(response.text, features='html.parser')
    results = soup.find('span', attrs={'data-component-type': 's-search-results'}).find_all(attrs={'data-component-type': 's-search-result'})

    print(len(results))

    for j in results:
        try:
            name = j.find('h2').text.strip()
            url = 'https://www.amazon.in' + j.find('h2').a.get('href')
            price = j.find(name='span', class_='a-price-whole').text.strip()
            rating = j.find(name='span', class_='a-size-base').text.strip()
            csvwriter.writerow([name, url, price, rating])
            print('Done')
        except Exception:
            print('Error occured')

# with open(file='web\\amazon\\2.html', mode='w', encoding='utf-8') as file:
#     file.write(str(results))

csvfile.close()