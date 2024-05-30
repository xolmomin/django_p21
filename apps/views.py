from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView

from apps.models import User


class MainTemplateView(TemplateView):
    template_name = 'apps/index.html'


class StudentListView(ListView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    template_name = 'apps/student/list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    template_name = 'apps/student/detail.html'
    context_object_name = 'student'


class StudentDeleteView(View):

    def get(self, request, pk):
        User.objects.filter(type=User.Type.STUDENT, id=pk).delete()
        return redirect('student_list_page')


class StudentUpdateView(UpdateView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    fields = 'first_name', 'last_name', 'email', 'birth_date', 'image'
    template_name = 'apps/student/edit.html'
    context_object_name = 'student'

    def get_success_url(self):
        return reverse('student_edit_page', kwargs={'pk': self.kwargs.get(self.pk_url_kwarg)})
