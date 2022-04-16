from django.urls import path
from .views import (
    CertificationListView, ExperienceListView,
    ExperienceDetailView, ExperienceFormView,ThanksView
)

app_name = 'certifications'

urlpatterns = [
    path('', CertificationListView.as_view(), name = 'certification_list'),
    path('experience_list/<int:pk>', ExperienceListView.as_view(), name = 'experience_list'),
    path('experience_detail/<int:pk>', ExperienceDetailView.as_view(), name = 'experience_detail'),
    path('experience_form/', ExperienceFormView.as_view(), name = 'experience_form'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
]