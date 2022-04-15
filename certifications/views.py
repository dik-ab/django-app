from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session
from django.urls import reverse_lazy
from .models import Certifications, Experiences
from django.http import JsonResponse
from . import forms
from .forms import ExperienceForm
import os

class CertificationListView(ListView):
    model = Certifications
    template_name = os.path.join('certifications', 'certification_list.html')

    def get_queryset(self):
        query = super().get_queryset()
        certification_name = self.request.GET.get('certification_name', None)
        if certification_name:
            query = query.filter(Q(name__icontains=certification_name))
            return query
        else:
            return None
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['certification_name'] = self.request.GET.get('certificaton_name', '')
        context['current_experience_list'] = Experiences.objects.all()
        return context


class ExperienceListView(ListView):
    model = Experiences
    template_name = os.path.join('certifications', 'experience_list.html')
    paginate_by=1

    def get_queryset(self, **kwargs):
        query = Experiences.objects.filter(certification__id=self.kwargs['pk'])
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        certification_name_list = Certifications.objects.get(id=self.kwargs['pk'])
        context['certification_name'] = certification_name_list.name
        return context


class ExperienceDetailView(DetailView):
    model = Experiences
    template_name = os.path.join('certifications', 'experience_detail.html')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        certification_name_list = Certifications.objects.get(experiences__id=self.kwargs['pk'])
        context['certification_name'] = certification_name_list.name
        return context



    
class ExperienceFormView(FormView):

    template_name = os.path.join('certifications', 'experience_form.html')
    form_class = forms.ExperienceForm
    success_url = reverse_lazy('certifications:certification_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(ExperienceFormView, self).form_valid(form)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ThanksView(TemplateView):
    template_name = os.path.join('certifications', 'thanks.html')

