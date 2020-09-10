import requests
import json


class SMMS(object):
    # init
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None
        self.profile = None
        self.history = None
        self.upload_history = None
        self.url = None

    # user
    def get_api_token(self):
        data = {
            'username': self.username,
            'password': self.password,
        }
        url = root+'token'
        res = requests.post(url, data=data).json()
        self.token = res['data']['token']
        self.headers = {'Authorization': self.token}
        # print(json.dumps(res, indent=4))

    # user
    def get_user_profile(self):
        url = root+'profile'
        res = requests.post(url, headers=self.headers).json()
        self.profile = res['data']
        print(json.dumps(res, indent=4))

    # image
    def clear_temporary_history(self):
        data = {
            'format': 'json'
        }
        url = root+'clear'
        res = requests.get(url, data=data).json()
        print(json.dumps(res, indent=4))

    # image
    def view_temporary_history(self):
        url = root+'history'
        res = requests.get(url).json()
        self.history = res['data']
        print(json.dumps(res, indent=4))

    # image
    def delete_image(self, hash):
        url = root+'delete/'+hash
        res = requests.get(url).json()
        print(json.dumps(res, indent=4))

    # image
    def view_upload_history(self):
        url = root+'upload_history'
        res = requests.get(url, headers=self.headers).json()
        self.upload_history = res['data']
        print(json.dumps(res, indent=4))

    # image
    def upload_image(self, path):
        try:
            files = {'smfile': open(path, 'rb')}
            url = root+'upload'
            res = requests.post(url, files=files, headers=self.headers).json()
            if res['success']:
                self.url = res['data']['url']
                # print(json.dumps(res, indent=4))
                print(self.url)
            else:
                print(res['message'])
        except Exception as e:
            print(e)


if __name__ == "__main__":
    root = 'https://sm.ms/api/v2/'
    smms = SMMS('username', 'password')
    smms.get_api_token()
    smms.upload_image('xxx.jpg')
