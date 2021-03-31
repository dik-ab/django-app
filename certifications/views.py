from django.shortcuts import render
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Certifications, Experiences
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
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['certification_name'] = self.request.GET.get('certificaton_name', '')
        return context


class ExperienceListView(ListView):
    model = Experiences
    template_name = os.path.join('certifications', 'experience_list.html')

    def get_queryset(self, **kwargs):
        # query = super(ExperienceListView, self).get_queryset(**kwargs)
        # pk = self.request.GET.get('pk')
        # if pk:
        #     query = query.filter(
        #         certification__id=pk
        #     )
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
        certification_name_list = Certifications.objects.get(id=self.kwargs['pk'])
        context['certification_name'] = certification_name_list.name
        return context

