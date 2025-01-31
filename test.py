import pytest
from main import get_random_cat_picture_info

def test_get_random_cat_picture_info(mocker):
   mock_get = mocker.patch('main.requests.get')
   mock_get.return_value.status_code = 200
   mock_get.return_value.json.return_value = {
       "id":"b5u",
       "url":"https://cdn2.thecatapi.com/images/b5u.jpg",
       "width":1024,
       "height":768
   }

   picture_info = get_random_cat_picture_info()
   assert picture_info == {
       "id":"b5u",
       "url":"https://cdn2.thecatapi.com/images/b5u.jpg",
       "width":1024,
       "height":768
   }

def test_get_random_cat_picture_info_with_error(mocker):
   mock_get = mocker.patch('main.requests.get')
   mock_get.return_value.status_code = 500

   user_data = get_random_cat_picture_info()
   assert user_data == None
