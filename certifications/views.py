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


class CertifiedExperienceView(DetailView):
    model = Experiences
    template_name = os.path.join('certifications', 'certified_experience.html')