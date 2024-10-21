import requests
from bs4 import BeautifulSoup
import csv


url = "https://vampirechronicles.fandom.com/wiki/Category:Characters_(Interview_with_the_Vampire_TV)"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
characters = soup.find_all("a", class_= 'category-page__member-link')

#with open('iwtv-characters.csv',mode = 'w',newline='', encoding = 'utf-8')as file:
    #writer = csv.writer(file)
   # writer.writerow(['name','status'])

with open('iwtv-characters.csv',mode = 'w',newline='', encoding = 'utf-8')as file:
        writer = csv.writer(file)
        writer.writerow(['name','status'])

for character in characters:
    #name = character.find('a',class_='Category:Characters').text
    #name = soup.select_one('h1').text.strip()
    name = character.get_text()
    status = character.find('span', class_='Category:Characters')
    if status == "alive":
        #aliveChar.append(name)
        status = "alive"
        #writer.writerow([name, status])
    else:
        #deadChar.append(name)
        status = "dead"
        #writer.writerow([name, status])
    with open('iwtv-characters.csv',mode = 'w',newline='', encoding = 'utf-8')as file:
        writer = csv.writer(file)
        writer.writerow(['name','status'])
        writer.writerow([name,status])
   
    # for index, row in writer.writerows('iwtv-characters.csv'):
               

#with open('iwtv-characters.csv',mode = 'w',newline='', encoding = 'utf-8')as file:
    #writer = csv.writer(file)
    #writer.writerow(['name','status'])
    #for character in charStatus:
    # for index, row in writer.writerows('iwtv-characters.csv'):
        #writer.writerow([name, status])


 

