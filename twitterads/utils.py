from django.conf import settings
from twython import Twython

app_key = settings.TWITTER_KEY
app_secret =settings.TWITTER_SECRET

def twitter_now(user, tweet):
    try:
        twitter = Twython(
        app_key = app_key,
        app_secret = app_secret,
        oauth_token = user.twitterprofile.oauth_token,
        oauth_token_secret = user.twitterprofile.oauth_secret
        )
        twitter.update_status(status=tweet.post)
        return True
    except:pass
