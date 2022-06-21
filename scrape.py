import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam/page-" #This is the address, after the dash sign will be using the for loop
with open("/content/drive/My Drive/house_full.csv", 'w',encoding='utf-8', newline='') as f: #This is a python file from google drive
    write = writer(f)
    head = ['Title', 'Location', 'Price', 'Area', 'Rooms', 'Interior'] #This is out dataframe
    write.writerow(head)
    for page in range(1,24): #There are 24 pages total
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
