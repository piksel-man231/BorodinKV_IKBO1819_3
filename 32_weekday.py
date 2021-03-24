import json
import email.utils
import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#with open('pract3/table.json', encoding='utf8') as f:
#    table = json.loads(f.read())  # Таблица решений задач

#with open('pract3/failed.json', encoding='utf8') as f:
#    failed = json.loads(f.read())  # Данные по ошибкам

with open('pract3/messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения

messages = [(email.utils.parsedate(m['date'])) for m in messages]#3899
print(messages[0])
x = []
day = []
for i in range(0, 3899):
    messages[i] = list(messages[i])
    del messages[i][8]
    del messages[i][7]
    del messages[i][6]
    del messages[i][5]
    del messages[i][4]
    del messages[i][3]
    x.append(datetime.datetime(messages[i][0],messages[i][1],messages[i][2]))
    day.append(x[i].strftime("%w"))
#print(messages[0])
#print(day[0])
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0
d7 = 0
for i in range(0,3899):
    if day[i] == "0":
        d7 = d7 + 1
    elif day[i] == "1":
        d1 = d1 + 1
    elif day[i] == "2":
        d2 = d2 + 1
    elif day[i] == "3":
        d3 = d3 + 1
    elif day[i] == "4":
        d4 = d4 + 1
    elif day[i] == "5":
        d5 = d5 + 1
    elif day[i] == "6":
        d6 = d6 + 1

#print(d7)
labels = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
men_means = [d1, d2, d3, d4, d5, d6, d7]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, label='Кол-во сдач')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

plt.show()