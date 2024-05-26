from django.urls import path

from apps.views import index_view, create_view

urlpatterns = [
    path('', index_view, name='index'),
    path('create', create_view, name='create_index')
]
