from django.test import TestCase, Client
from django.urls import reverse
from certifications.views import (
    CertificationListView, 
    ExperienceListView, 
    ExperienceDetailView, 
    ExperienceFormView,
)