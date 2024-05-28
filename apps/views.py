from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from math import ceil

from apps.models import Product, Category, User


class MainTemplateView(TemplateView):
    template_name = 'apps/index.html'


class StudentListView(ListView):
    queryset = User.objects.filter(type=User.Type.STUDENT)
    template_name = 'apps/student/list.html'
    context_object_name = 'students'
