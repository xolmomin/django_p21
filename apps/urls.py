from django.urls import path
from apps.views import MainTemplateView, StudentDeleteView, StudentUpdateView, StudentListView, StudentDetailView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),
    path('student/delete/<int:pk>', StudentDeleteView.as_view(), name='student_delete_page'),
    path('student/edit/<int:pk>', StudentUpdateView.as_view(), name='student_edit_page'),
    path('student/detail/<int:pk>', StudentDetailView.as_view(), name='student_detail_page'),
    path('student/list', StudentListView.as_view(), name='student_list_page')
]
