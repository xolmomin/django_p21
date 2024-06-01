from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, resolve_url
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

from apps.forms import CustomUserCreationForm
from apps.models import User


class MainTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/index.html'
    # login_url = reverse_lazy('login_page')


class StudentListView(LoginRequiredMixin, ListView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    template_name = 'apps/student/list.html'
    context_object_name = 'students'
    paginate_by = 3


class StudentDetailView(LoginRequiredMixin, DetailView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    template_name = 'apps/student/detail.html'
    context_object_name = 'student'


class StudentCreateView(LoginRequiredMixin, CreateView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    fields = 'username', 'gender', 'type', 'first_name', 'last_name', 'birth_date', 'image', 'password'
    template_name = 'apps/student/edit.html'
    success_url = reverse_lazy('student_list_page')
    context_object_name = 'student'


class StudentDeleteView(LoginRequiredMixin, View):

    def get(self, request, pk):
        User.objects.filter(type=User.Type.STUDENT, id=pk).delete()
        return redirect('student_list_page')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    fields = 'first_name', 'last_name', 'email', 'birth_date', 'image'
    template_name = 'apps/student/edit.html'
    context_object_name = 'student'

    def get_success_url(self):
        return reverse('student_edit_page', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})


class TeacherListView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/teacher/list.html'


class RegisterView(CreateView):
    template_name = 'apps/auth/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login_page')


class CustomLoginView(LoginView):
    template_name = 'apps/auth/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user: User = self.request.user
        if user.type == User.Type.STUDENT:
            return resolve_url('student_list_page')
        return resolve_url('main_page')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_page')
