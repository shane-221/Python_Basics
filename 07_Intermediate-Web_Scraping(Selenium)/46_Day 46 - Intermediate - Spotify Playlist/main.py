import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
from dotenv import load_dotenv
load_dotenv()

year= input("Which year do you want to travel to? Type the date in this format - YYYY-MM-DD : ")
#---------------------------------------- Variables-------------------------------------------------------------------#
USER_AGENT ="Windows NT 10.0; Win64; x64"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


#-------------------------------------Get the songs list  by web scraping ---------------------------------------------#
# Todo: get the website data
data = requests.get(url=  f"https://www.billboard.com/charts/hot-100/{year}", headers= header )
website = data.text

# Todo: Scraping the Website
soup = BeautifulSoup(website, "html.parser")
        # Pull all the 100 items
song_block =  soup.find_all( name = "div",
                        class_ = "o-chart-results-list-row-container"
                        )
song_names =[]
for i in song_block:
    heading = i.find(name ="h3")
    song_names.append(heading.get_text(strip= True))

#-----------------------------Spotipy: connect to spotify and get username --------------------------------------------#
# Since the code isw being run on behalf of a user. Need to specifically use a module that allows you to interact
##w with someone's account
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
                    client_id= os.getenv("client_id"),
                    redirect_uri=os.getenv("redirect_uri"),
                    client_secret=os.getenv("client_secret"),
                    scope= "playlist-modify-private"
                                    ))
user_id = sp.current_user()["id"]



#-------------------------------------Search Spotify for the Songs-----------------------------------------------------#
uri_list = []

for song in song_names:
    try:
        search = sp.search(q=f"{song}:{year}", type="track")
        uri = search["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except Exception as e:
        print(f" Not Found. Error Code: {e}")



# #-------------------------------------Adding the songs to the Playlist-------------------------------------------------#
## The billboard is the app. Therefore, need to create the app within the playlist.
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)

sp.playlist_add_items(
                        playlist_id=playlist["id"],
                        items =uri_list
                            )
