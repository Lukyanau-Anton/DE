'''
В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица.
Просуммируйте все числа в ней и введите в качестве ответа одно число - эту сумму
Для доступа к ячейкам используйте возможности BeautifulSoup.
'''

import requests
from bs4 import BeautifulSoup

r = requests.get('https://stepik.org/media/attachments/lesson/209723/3.html')

r.encoding = 'utf-8'
res = r.text

soup = BeautifulSoup(res, 'html.parser')

res = []
for i in soup.find_all('td'):
    res.append(int(i.text))

print(sum(res))
