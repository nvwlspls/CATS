from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from shows.views import viewEditHome


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lview.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url for viewing the list of all listings belongin to  one study 
    url(r'^$', viewEditHome.as_view(), name = 'editHome'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


