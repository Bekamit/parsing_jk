# import requests
# from bs4 import BeautifulSoup
# import csv

# URL = 'https://enter.kg/computers/noutbuki_bishkek'

# def write_to_csv(data):
#     with open('data.csv','a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'],data['price'],data['image']])

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BeautifulSoup(html,'lxml')
#     list_comp = soup.find_all('div',class_ = 'row')


#     for comp in list_comp:
#         title = comp.find('span',class_ = 'prouct_name').text
#         price = comp.find('span', class_ = 'price').text
#         image =  'https://enter.kg/' + comp.find('img').get('src')
#         dict_ = {'title':title,'price':price,'image':image}
#         write_to_csv(dict_)

# print(get_data(get_html(URL)))

# import requests
# from bs4 import BeautifulSoup
# import csv

# URL = 'https://vesti.kg'

# def write_to_csv(data):
#     with open('data4.csv','a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title']])

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BeautifulSoup(html,'lxml')
#     list_title = soup.find_all('div',class_ = 'itemContainer itemContainerLast')


#     for title_ in list_title:
#         title = title_.find('h2').text
#         dict_ = {'title':title}
#         write_to_csv(dict_)

# print(get_data(get_html(URL)))


# import requests
# from bs4 import BeautifulSoup
# import csv

# count = 0

# while count <= 3000:

#     URL = f'https://vesti.kg/itemlist.html?start={count}'

#     def write_to_csv(data):
#         with open('data4.csv','a') as file:
#             writer = csv.writer(file)
#             writer.writerow([data['title']])

#     def get_html(url):
#         response = requests.get(url)
#         return response.text

#     def get_data(html):
#         soup = BeautifulSoup(html,'lxml')
#         list_title = soup.find_all('div',class_ = 'itemContainer itemContainerLast')


#         for title_ in list_title:
#             title = title_.find('h2').text
#             dict_ = {'title':title.strip()}
#             write_to_csv(dict_)

#     print(get_data(get_html(URL)))

#     count += 30


# import requests
# from bs4 import BeautifulSoup
# import csv

# count = 0

# while count <= 2:

#     URL = f'http://kenesh.kg/ru/news/all/list?page={count}'

#     def write_to_csv(data):
#         with open('jk.csv','a') as file:
#             writer = csv.writer(file)
#             writer.writerow([data['images']])

#     def get_html(url):
#         response = requests.get(url)
#         return response.text

#     def get_data(html):
#         soup = BeautifulSoup(html,'lxml')
#         list_image = soup.find_all('img',class_ = 'news__item__image__img')


#         for image in list_image:
#             imgage_ = image.get('src')
#             dict_ = {'images':imgage_}
#             write_to_csv(dict_)

#     print(get_data(get_html(URL)))

#     count += 1

import requests
from bs4 import BeautifulSoup
import csv

count = 1

while count <= 100:

    URL = f'http://kenesh.kg/ru/news/all/list?page={count}'

    def write_to_csv(data,data2,data3):
        with open('jk.csv','a') as file:
            writer = csv.writer(file)
            writer.writerow([data['date'],data2['images'],data3['title']])

    def get_html(url):
        response = requests.get(url)
        return response.text

    def get_data(html):
        soup = BeautifulSoup(html,'lxml')
        list_date = soup.find_all('div',class_ = 'news__item news__item__3')
        list_image = soup.find_all('img',class_ = 'news__item__image__img')
        list_title = soup.find_all('h3',class_ = 'news__item__title')


        for date in list_date:
            date_ = date.find('div',class_ = 'news__item__date').text
            dict_ = {'date':date_}

        for image in list_image:
            imgage_ = image.get('src')
            dict2_ = {'images':imgage_}
        
        for title in list_title:
            title_ = title.find('a',class_ = 'news__item__title__link').text
            dict3_ = {'title':title_}

            write_to_csv(dict_,dict2_,dict3_)

    print(get_data(get_html(URL)))

    count += 1
