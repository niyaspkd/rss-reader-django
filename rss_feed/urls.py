from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'feed_reader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/login/$', 'rss_feed.views.login'),
    url(r'^accounts/auth/$', 'rss_feed.views.auth_view'),
    url(r'^accounts/logout/$', 'rss_feed.views.logout'),
    url(r'^accounts/loggedin/$', 'rss_feed.views.loggedin'),
    url(r'^accounts/invalid/$', 'rss_feed.views.invalid_login'),
    url(r'^accounts.register/$', 'rss_feed.views.register_user'),
    

    url(r'^admin/', include(admin.site.urls)),
)
