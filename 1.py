import requests
import csv
import threading
import time

file = open('amazon.csv')
read = csv.reader(file)
head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}

def getdata(info):
    res = requests.get(f'https://www.amazon.{info[3]}/dp/{info[2]}', headers=head)
    print(res.status_code, info)

for i in read:
    threading.Thread(target=getdata, args=[i]).start()
    time.sleep(0.5)

file.close()
print('Finish')
