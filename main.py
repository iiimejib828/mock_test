import requests

def get_random_cat_picture_info():
   url = 'https://api.thecatapi.com/v1/images/search'
   response = requests.get(url)
   if response.status_code == 200:
       return response.json()
   else:
       return None
