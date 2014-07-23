from django.db import models
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField

Tweet_TYPE = (('GT','Greetings'),('PT','Promotion'))

class Media(models.Model):
    images = ThumbnailerImageField('Images', upload_to='images')

    def __unicode__(self):
        return 'Tweet Images'
    
class Tweets(models.Model):
    post = models.CharField('Post', max_length = 140)
    start_date = models.DateField('Start Date', null=True, blank=True)
    end_date = models.DateField('End Date', null=True, blank=True)
    start_time = models.TimeField('Start Time', max_length=25, null=True, blank=True)
    end_time = models.TimeField('End Time', max_length=25, null=True, blank=True)
    task_id = models.CharField('Task', max_length = 80, null=True, blank=True)
    image =  models.ForeignKey(Media, related_name='tweet_media', null=True, blank=True)
    type = models.CharField(max_length=2,choices=Tweet_TYPE)
    created_on = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User,related_name='user_tweets')
    
    def __unicode__(self):
        return self.post


