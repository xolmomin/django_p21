from django.urls import path
from apps.views import MainTemplateView, StudentListView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),
    path('student/list', StudentListView.as_view(), name='student_list_page')
]
