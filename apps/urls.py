from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.views import index_view, main_view, member_view
from root.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('', main_view, name='main'),
    path('index', index_view, name='index'),
    path('member', member_view)
]