from google.colab import drive
drive.mount("/content/drive")
import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam/page-"
with open("/content/drive/My Drive/house_full.csv", 'w',encoding='utf-8', newline='') as f:
    write = writer(f)
    head = ['Title', 'Location', 'Price', 'Area', 'Rooms', 'Interior']
    write.writerow(head)
    for page in range(1,24):
      html = requests.get(url+str(page))
      soup = BeautifulSoup(html.content,'html.parser')
      lists = soup.find_all('section', class_="listing-search-item")
      for list in lists:
        title = list.find('a', class_="listing-search-item__link--title").text.replace('\n','')
        location = list.find('div', class_="listing-search-item__location").text.replace('\n','')
        price = list.find('div', class_="listing-search-item__price").text.replace('\n','')
        features_surface_area = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area").text.replace('\n','')
        features_number_of_rooms = list.find('li', class_="illustrated-features__item illustrated-features__item--number-of-rooms").text.replace('\n','')
        features_interior = list.find('li', class_="illustrated-features__item illustrated-features__item--interior")
        features_interior = 'None' if features_interior is None else features_interior.text.replace('\n','')
        form = [title, location, price, features_surface_area, features_number_of_rooms,features_interior]
        write.writerow(form)  
    
