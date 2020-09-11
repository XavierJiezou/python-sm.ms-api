# python-sm.ms-api
This is a python implementation of sm.ms api. sm.ms is a site where you can upload the image and get its url.
# usage
1. enter the https://sm.ms/
2. register and login
3. don't forget your username and password
```
if __name__ == "__main__":
    root = 'https://sm.ms/api/v2/'
    smms = SMMS('username', 'password')
    smms.get_api_token()
    smms.upload_image('xxx.jpg')
```
