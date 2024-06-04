from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, resolve_url
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView

from apps.forms import CustomUserCreationForm
from apps.models import User
from apps.tokens import account_activation_token
from apps.utils import generate_one_time_verification


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

    def form_valid(self, form):
        user = form.save()
        generate_one_time_verification(self.request, user)
        text = "<h3>An email has been sent with instructions to verify your email</h3>"
        messages.add_message(self.request, messages.SUCCESS, text)
        return super().form_valid(form)


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


class VerifyEmailConfirm(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your email has been verified.')
            return redirect('login_page')
        else:
            messages.warning(request, 'The link is invalid.')
        return redirect('register_page')
