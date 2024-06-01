from django.urls import path

from apps.views import MainTemplateView, StudentDeleteView, StudentUpdateView, StudentListView, StudentDetailView, \
    TeacherListView, StudentCreateView, RegisterView, LogoutView, CustomLoginView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main_page'),

    path('student/add', StudentCreateView.as_view(), name='student_add_page'),
    path('student/delete/<int:pk>', StudentDeleteView.as_view(), name='student_delete_page'),
    path('student/edit/<int:pk>', StudentUpdateView.as_view(), name='student_edit_page'),
    path('student/detail/<int:pk>', StudentDetailView.as_view(), name='student_detail_page'),
    path('student/list', StudentListView.as_view(), name='student_list_page'),

    path('teacher/list', TeacherListView.as_view(), name='teacher_list_page'),

    path('logout', LogoutView.as_view(), name='logout_page'),
    path('login', CustomLoginView.as_view(), name='login_page'),
    path('register', RegisterView.as_view(), name='register_page'),
]
