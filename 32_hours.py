import json
import email.utils
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
for i in range(0, 3899):
    j=i*10
    messages[j] = list(messages[j])
    del messages[j][8]
    del messages[j][7]
    del messages[j][6]
    del messages[j][5]
    del messages[j][2]
    del messages[j][1]
    del messages[j][0]
    x = messages[j][0]
    y = messages[j][1]
    s = 100
    plt.scatter(x, y, s, c="b", alpha=0.5)
plt.xlabel("Часы")
plt.ylabel("Минуты")
plt.show()
print(messages[0])
