 import requests
 from bs4 import BeautifulSoup
 import csv
 from time import sleep
 from random import randint
 file = open('movies.csv', 'w', newline='\n')
  header = 'Title,Year,Ranking\n'
  file.write(header)
 file_obj = csv.writer(file)
 header = ['Title', 'Year', 'Ranking']
 file_obj.writerow(header)

 ind = 1
 while ind<=250:
     url = 'https://www.imdb.com/search/title/?groups=top_250&start=3' + str(ind)
     h = {'Accept-Language':'en-US'}
     r = requests.get(url, headers=h)
     # print(r.status_code)
     content = r.text
     soup = BeautifulSoup(content, 'html.parser')
     # movies_block = soup.find('div', {'class':'lister-list'})
     movies_block = soup.find('div', class_='lister-list')
     all_movies = movies_block.find_all('div', class_='lister-item')
     for each in all_movies:
         title = each.h3.a.text
         year = each.find('span', class_='lister-item-year').text
         year = year.replace('(', '')
         year = year.replace(')', '')
         ranking = each.strong.text
         print(ranking)
         # file.write(title+','+year+','+ranking+'\n')
         file_obj.writerow([title, year, ranking])
     ind += 70
     sleep(randint(15,20))

 file.close()
