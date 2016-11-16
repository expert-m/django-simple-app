from django.conf.urls import url

from core.views import HomeView, SearchView, ProviderView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^provider/(?P<id>[0-9]+)/$', ProviderView.as_view(), name='provider'),
]
