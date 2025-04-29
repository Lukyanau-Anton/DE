'''
В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица
Просуммируйте все числа в ней
Теперь мы добавили разных тегов для изменения стиля отображения.
Для доступа к ячейкам используйте возможности BeautifulSoup.
'''

import requests
from bs4 import BeautifulSoup

r = requests.get('https://stepik.org/media/attachments/lesson/209723/4.html')

r.encoding = 'utf-8'
res = r.text
soup = BeautifulSoup(res, 'html.parser')

al = soup.find_all('td')

res = []

for item in al:
    res.append(int(item.string))
print(sum(res))
