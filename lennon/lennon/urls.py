from django.conf.urls import include, url
from django.contrib import admin
from gametime import urls as g_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'lennon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', ' gametime.views.index', name='index'),
    url(r'^', include(g_urls)),
]
