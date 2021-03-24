import json
import email.utils

with open('pract3/messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения
a = []
messages = [(m['subj'].upper()) for m in messages]
print(messages[0])
data = []
for i in range(0, 3899):
    messages[i] = list(messages[i])
    del messages[i][-1]
    del messages[i][-1]
    data.append(0)
    messages[i][-2].add(messages[i][-1])
    data[i] = (messages[i][0], messages[i][1])
print(messages[0])
print(data[0])
