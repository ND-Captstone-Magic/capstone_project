import requests
import json
import pandas as pd

url = 'https://api.foursquare.com/v2/venues/explore'
url2 = 'https://api.foursquare.com/v2/venues/categories'
url3 ='https://api.foursquare.com/v2/venues/search'

CLIENT_ID='UGPV5HR24VYYNI5PYM1Q3JE0ABDYOOZ454F4H3J24JCE4FGO'
CLIENT_SECRET='ONGSEUBMYX5KJ3NXYE4DN0MDSW5S2LGYBZA3X3EWXVS3DFZB'
GEO='37.444572,-122.160309'
CATEGORY=''
DATE='20211117' #YYYYMMDD

search_url= f'https://api.foursquare.com/v2/venues/search?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&ll={GEO}&query={CATEGORY}&v={DATE}'

resp = requests.get(url=search_url)

data = resp.json()

columns = ['name', 'lat', 'lon', 'categories']
venue_name_list = []
latitude_list = []
longitude_list = []
categories_list = []

for i in data['response']['venues']:
    venue_name_list.append(i['name'])
    latitude_list.append(i['location']['lat'])
    longitude_list.append(i['location']['lng'])
    
    for k in i['categories']:
        categories_list.append(k['name'])
        #print('Category: ' + k['name'] + '\n')

# dictionary of lists 
dict_for_df = {'name': venue_name_list, 'category': categories_list, 'lat': latitude_list, 'lon': longitude_list} 
    
df = pd.DataFrame(dict_for_df)
    
print(df) 

