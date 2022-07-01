import requests
import os
import lxml
import spotipy.util as util
from pprint import pprint
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import spotipy
from spotipy.oauth2 import SpotifyOAuth
old_skool = []
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=os.environ.get("client_id"),client_secret=os.environ.get("client_secret")))
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ.get("client_id"),
        client_secret=os.environ.get("client_secret"),
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.text"))
# token = util.prompt_for_user_token(username="Rando Yellow",client_id=os.environ.get("client_id"),client_secret=os.environ.get("client_secret"),redirect_uri="http://example.com",scope="playlist-modify-public user-library-read playlist-modify-public user-library-modify user-library-read user-library-modify")
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ.get("client_id"),client_secret=os.environ.get("client_secret")))
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("client_id"),client_secret=os.environ.get("client_secret"),redirect_uri="http://example.com",scope="313rul42mffoab2t4ikeirfy74lm"))

# spotify_details = [Client ID 526da233027644468862b1ca29fb105d Client Secret 6eef51b7ac874444bc71a061adfb9823]

# results = sp.search(q='...Baby One More Time', limit=20)
url = "https://www.billboard.com/charts/hot-100/1999-02-20/"
ding= "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
mew = "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
wow = "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

raw_soup = requests.get(url)
raw_soup = raw_soup.text
cooked_soup = BeautifulSoup(raw_soup,"lxml")
# elemental = cooked_soup.find_all("h3",id="title-of-a-story")
elemental = cooked_soup.find_all(class_="c-title", id="title-of-a-story")
del(elemental[3:6])
# del(elemental[3])

# print(elemental[4].text.strip())
# print(cooked_soup.prettify())
n = 0
for amily in elemental:
    n+=1
    # print(n)
    if n%4 == 0:
        oldie = (amily.text.strip())
        old_skool.append(oldie)
    elif n>400:
        break
users = (spotify.current_user()["id"])

try1 = spotify.search(q="pakurumo",limit=5)
# pprint(try1)
# print(old_skool)
final_spotify = []
for song in old_skool:
    trials = spotify.search(q=song,limit=5)
    finals = (trials["tracks"]["items"][0]["uri"])
    final_spotify.append(finals)

# pprint(final_spotify)
new_list = spotify.user_playlist_create(name="oldies",user=users,public=False,collaborative=False,description="Old Skool Lapel")
playlist_id = (new_list["id"])
print(playlist_id)
m = 0
for mango in final_spotify:
    banana = []
    # print(mango)
    ban = ((mango.split(":")[2]))
    banana.append(ban)
    player = spotify.playlist_add_items(playlist_id=playlist_id,items=banana,position=m)
    # print(banana)
    m+=1



