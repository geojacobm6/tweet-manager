from django.contrib import admin

from twitterads.models import Tweets

class TweetsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tweets, TweetsAdmin)