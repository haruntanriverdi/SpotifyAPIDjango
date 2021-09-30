import os

from django.shortcuts import render, redirect
import requests, json
import base64
import random
from requests.exceptions import HTTPError
from .forms import GenreForm

json_file = open('genres.json', )
# convert a dictionary
json_data = json.load(json_file)

json_file.close()


def GenerateToken():
    clientId = os.getenv('CLIENT_ID')
    clientSecret = os.getenv('CLIENT_SECRET')

    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')

    credential = requests.post('https://accounts.spotify.com/api/token',
                               headers={
                                   'Authorization': 'Basic ' + base64Message
                               },
                               data={
                                   "grant_type": 'client_credentials'
                               })
    token = credential.json()

    return token, credential.status_code


token, status_code = GenerateToken()


def HomeView(request):
    msg_success = None
    msg_fail = None
    success = False

    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            return redirect('track', request.POST['genres'])
    else:
        form = GenreForm()
        return render(request, "Home.html", {"form": form, "msg_fail": msg_fail, })


def TrackView(request, genre):
    global token
    track_list = []

    random_artist = random.choice(json_data[genre])
    # print(random_artist)
    msg_success = None
    msg_fail = None
    success = False

    try:
        if status_code == '401':
            token, response_code = GenerateToken()
            msg_fail = f'Token may be expire. Retrying to get access token...'

        access_token = token['access_token']

        artist_info = requests.get(
            'https://api.spotify.com/v1/search',
            headers={'Authorization': 'Bearer ' + access_token},
            params={'q': random_artist, 'type': 'track', 'limit': 50, 'market': 'TR', 'include_external': 'audio'})

        json_response = artist_info.json()
        # print(json_response)
        for data in json_response['tracks']['items']:
            album_image = data['album']['images'][2]['url']
            track_name = data['name']
            track_popularity = data['popularity']
            track_preview = data['preview_url']

            track_list.append((track_name, track_popularity, track_preview, album_image))
            track_list.sort(key=lambda x: int(x[1]), reverse=True)

            track_list = track_list[:10]

    except HTTPError as httpError:
        msg_fail = f'HTTP error occured: {httpError}'
    except KeyError as keyError:

        msg_fail = f'Key error occured. Please check client information: {keyError}'
    except Exception as err:

        msg_fail = f'Other error occured: {err}'

    return render(request, 'Track.html',
                  {'track_list': track_list, 'msg_fail': msg_fail, 'random_artist': random_artist.capitalize()})
