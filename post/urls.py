from django.conf.urls import url

from .views import PostLV

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='list'),
]
