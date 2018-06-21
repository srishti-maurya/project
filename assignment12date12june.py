#solution to question number 1

access token:

An access token is an object that describes the security context of a process or thread.
The information in a token includes the identity and privileges of the user account associated with the process or thread.

access token for api:

	https://api.twitter.com/oauth/access_token

#solution to question number 2

nslookup google.com
ip address 2404:6800:4009:80d::200e
           172.217.166.78

nslookup facebook.com
ip address 2a03:2880:f12f:83:face:b00c:0:25de
           157.240.16.35

#solution to question number 3

#sudo pip install tweepy
import tweepy
consumer_key=................
consumer_secret=...........................
access_token=........................
access_token_secret=..........................
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
status="testing"
api.update_status(status=status)

#solution to question number 4

API is a part of library which denes how an application communicates with external code.
API can be written in any language.
Library is written in same language which is a collection of all the functionalities required
for the use case.
For example : Numpy is a library of Python, adding support for large, multi-dimensional
arrays and matrices, along with a large collection of high-level mathematical functions to
operate on these arrays.

#solution to question number 5

import spotipy

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify()
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print 'track    : ' + track['name']
    print 'audio    : ' + track['preview_url']
    print 'cover art: ' + track['album']['images'][0]['url']

