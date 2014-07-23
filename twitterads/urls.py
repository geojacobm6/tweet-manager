from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from twitterads.views import TweetList, GreetingCreate, TweetFeatures, DeleteList, PostTweet

urlpatterns = patterns('apps.ContactLists.views',

        url(r'^features/$', TweetFeatures.as_view(),name='tweet_feature'),
        url(r'^add/$', login_required(GreetingCreate.as_view()),name='add_greetings'),
        url(r'^list/$', TweetList.as_view(),name='tweet_list'),
        url(r'^delete/(?P<pk>\d+)/$', DeleteList.as_view(),name='tweet_delete'),
        url(r'^add-n-tweet/$', login_required(PostTweet.as_view()),name='add_n_tweet'),
     )