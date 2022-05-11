import tweepy
import os

#enter your keys from twitter
API_key = "______"
API_key_secret = "________"

Access_Token = "_______"
Access_Token_secret = "________"

auth = tweepy.OAuth1UserHandler(API_key, API_key_secret)
auth.set_access_token(Access_Token,Access_Token_secret)

api = tweepy.API(auth)

# Upload image
img = "image location"
media = api.media_upload(img)
 
 # Post tweet with image
tweet = "caption for your post"
post_result = api.update_status(status=tweet, media_ids=[media.media_id])
 



