from __future__ import absolute_import

from django.conf import settings
from celery import states
from celery.exceptions import Ignore
from networkingads.celery import app
from twython import Twython

app_key = settings.TWITTER_KEY
app_secret =settings.TWITTER_SECRET

    
@app.task(bind=True)
def send_twitter_status(self, user, tweet):
    try:
        twitter = Twython(
        app_key = app_key,
        app_secret = app_secret,
        oauth_token = user.twitterprofile.oauth_token,
        oauth_token_secret = user.twitterprofile.oauth_secret
        )
        twitter.update_status(status=tweet.post)
    except:
        raise self.retry()


@app.task(bind=True)
def get_tweets(self, user):
    timeline = twitter.get_timeline(user)
    self.update_state(state=states.SUCCESS, meta=timeline)
    raise Ignore()