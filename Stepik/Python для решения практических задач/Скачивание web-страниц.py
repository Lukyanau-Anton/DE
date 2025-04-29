"""
Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще Python или C++ (ответ должен быть одной из этих двух строк).
"""
import requests

r = requests.get('https://stepik.org/media/attachments/lesson/209717/1.html')
r.encoding = 'utf-8'
print(r.text.count('Python'), r.text.count('C++'), sep='\n')
