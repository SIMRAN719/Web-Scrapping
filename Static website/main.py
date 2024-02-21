import csv
import requests
from bs4 import BeautifulSoup

url='https://www.espncricinfo.com/cricketers'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')

data=[]
names=soup.find_all(class_='ds-text-tight-l')
ages=soup.find_all(class_='ds-text-tight-m ds-font-regular ds-text-typo-mid3')
for name,age in zip(names,ages):
    temp={}
    x=name.get_text()
    y=age.get_text()[5:7]
    temp['Name']=x
    temp['Age']=int(y)
    data.append(temp)

csv_file='data.csv'
col_titles=data[0].keys()
f=open(csv_file,'w',newline='')
writer=csv.DictWriter(f,fieldnames=col_titles)
writer.writeheader()
for row in data:
    writer.writerow(row)