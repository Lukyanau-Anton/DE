'''
Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python. В этой статье есть теги
code, которыми выделяются конструкции на языке Python. Вам нужно найти все строки, содержащиеся между тегами <code> и
</code> и найти те строки, которые встречаются чаще всего и вывести их в алфавитном порядке, разделяя пробелами.
'''

import requests
import re

r = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html')
r.encoding = 'utf-8'
res = r.text

str = re.findall(r'<code>(.*?)</code>', res)

c = []
for i in str:
    c.append(str.count(i))
res = dict(zip(str, c))

z = []
for k, v in res.items():
    if v == max(res.items(), key=lambda i: i[1])[1]:
        z.append(k)
z.sort()
print(*z)

