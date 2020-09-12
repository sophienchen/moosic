#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Authorization
#Get top artists
#Get related artists
#Take all artists + related artists’ songs and match with mood
#Add tracks to playlist

#import spotify_id
import json
import requests

class CreatePlaylist:
    
    def authorization():
        pass
    def top_artists(self):
        # curl -X GET "https://api.spotify.com/v1/me/top/artists" -H "Authorization: Bearer {your access token}"
        # GET https://api.spotify.com/v1/me/top/artists
        pass
    def related_artists(self):
        #GET https://api.spotify.com/v1/artists/{id}/related-artists
        pass
    def create_playlist(self):
        request_body = json.dumps({
            "name": "Mood Playlist",
            "description": "Playlist generated to match your mood!",
            "public": True
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # playlist id
        return response_json["id"]
    
    def get_spotify_uri(self, song_name, artist):
        """Search For the Song"""
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # only use the first song
        uri = songs[0]["uri"]

        return uri
    
    def mood_match():
        pass
    
    def add_tracks(self):
        # collect all of uri- edit after implementing mood_match
        uris = [info["spotify_uri"]
                for song, info in self.all_song_info.items()]
        
        # create playlist
        playlist_id = self.create_playlist
        
        # add songs
        request_data = json.dumps(uris)

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

        response = requests.post(
            query,
            data=request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )
        response_json = response.json()
        return response_json