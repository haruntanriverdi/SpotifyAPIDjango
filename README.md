# Django Spotify Search API
Django  HTTP request using Spotify API. 

## Usage
- Install virtualenv
```
cd path/to/project/folder
```

- Install virtualenv

```
$ pip install virtualenv
$ virtualenv venv
$ cd venv
$ source bin/activate
```

- Install requirements

```
$ pip install -r requirements.txt
```
- You can run the application with the following command:

```
$ python manage.py runserver
```
## Configuration
- You need to configure SECRET_KEY, CLIENT_ID, CLIENT_SECRET. To do this:

1- Create .env file in project folder

2- Write SECRET_KEY, CLIENT_ID, CLIENT_SECRET  save:

```
SECRET_KEY= seret_key
CLIENT_ID = spotify_client_id
CLIENT_SECRET = spotify_client_secret
```
