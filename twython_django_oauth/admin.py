from django.contrib import admin

from twython_django_oauth.models import TwitterProfile

class TwitterProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(TwitterProfile, TwitterProfileAdmin)