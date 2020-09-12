# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
import spotipy
import config
from spotipy.oauth2 import SpotifyClientCredentials
import os
import spotipy.util as util

# CID = os.environ['client']
# CSECRET = os.environ['secret']
token = util.prompt_for_user_token(
        username=config.USER,
        scope="user-library-read",
        client_id=config.CID,
        client_secret=config.CSECRET,
        redirect_uri="https://moosic-pennapps.herokuapp.com/")
sp = spotipy.Spotify(auth=token.get_access_token())
results = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')
print (results)
# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])
# -- Initialization section --
app = Flask(__name__)

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"}
    ]


# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="0afcbed18eca4513969f0c55e644d436",
#                                                            client_secret="ef2e850623ba4799b77fdb7dc85f2c14"))

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

# name of database
# app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
# app.config['MONGO_URI'] = 'mongo-uri'

# mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
        return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database

    # insert new data

    # return a message to the user
    return ""
