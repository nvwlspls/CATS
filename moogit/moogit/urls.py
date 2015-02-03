from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from shows.views import homePage, viewEditHome

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moogit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homePage.as_view(), name = 'home'),
    url(r'^edit/', viewEditHome.as_view(), name = 'editHome'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
