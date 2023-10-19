import json
import requests

class Pets:
    """API библиотека к сайту http://34.141.58.52:8080/#/"""
    """API library for http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Запрос в Swagger сайта получения уникального токена пользователя по указанным почте и паролю"""
        """Request in Swagger of the site to obtain a unique user token using the specified email and password"""
        data = {"email": 'ololo123@gmail.com',
                "password": '123456'}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']  #
        my_id = res.json()['id']
        status = res.status_code
        print(my_token)
        print(res.json())
        return my_token, status, my_id

    def get_list_users(self) -> json:
        """Запрос в сваггер сайта на получение списка пользователей."""
        """Request to the site swagger to receive a list of users."""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        my_id = res.status_code
        return status, my_id

    def create_pet(self) -> json:
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {'name': 'Slow',
                'type': 'reptile',
                'age': 27,
                'owner_id': my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        print(pet_id)
        print(res.json())
        return pet_id, status

    def get_pet_photo(self) -> json:
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': ('reptile.jpg', open(r'D:\STUDY\AQApython\Pets_project_api\photos\reptile.jpg', 'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        print(res.json())
        return status, link

    def update_pet(self) -> json:
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id,
                "name": 'Slow',
                "type": 'reptile',
                "age": 28,
                "owner_id": my_id}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def like_pet(self) -> json:
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        return status, pet_id

    def delete_pet(self) -> json:
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status



#To run a specific function, comment out the others
Pets().get_token()
Pets().get_list_users()
Pets().create_pet()
Pets().get_pet_photo()
Pets().update_pet()
Pets().like_pet()
Pets().delete_pet()
