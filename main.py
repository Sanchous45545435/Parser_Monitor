import requests
from bs4 import BeautifulSoup
import lxml
import fake_user_agent


user = fake_user_agent.UserAgent().random

headers = {'user-agent': user}

session = requests.Session()

page = int(input('Input page '))
url_input = input('Input URL categories ')
for j in range(1, page+1):
    url = f'{url_input}p-{j}'
    response = session.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    all_product = soup.find('div', class_='catalog-grid ng-star-inserted')
    product_list = all_product.find_all('div', class_='catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted')
    for i in range(len(product_list)):
        product = product_list[i].find('a', class_='goods-tile__heading ng-star-inserted').text
        url_product = product_list[i].find('a', {"href": "/currencies/bitcoin/markets/"})
        try:
            old_price = product_list[i].find('div', class_='"goods-tile__price--old price--gray ng-star-inserted').text
            new_price = product_list[i].find('div', class_='goods-tile__price price--red ng-star-inserted').text
            with open('myproduct.txt', 'a', encoding='UTF-8') as file:
                file.write(f"{product}   Old price  {old_price} New price {new_price}'\n'")
        except AttributeError:
            print('Old price no!')
    print(f"Закончил {j} страницу")