from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from networkingads.views import HomeView

admin.autodiscover()
urlpatterns = [
    # ... the rest of your URLconf goes here ...
    url(r'^$', HomeView.as_view()),
#     # url(r'^blog/', include('blog.urls')),
#
    url(r'^tweet/', include('twitterads.urls')),
    url(r'^twitter/', include('twython_django_oauth.urls')),
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
