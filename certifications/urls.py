from django.urls import path
from .views import (
    CertificationListView, CertifiedExperienceView,
)

app_name = 'certifications'

urlpatterns = [
    path('certification_list/', CertificationListView.as_view(), name = 'certification_list'),
    path('certified_experience/<int:pk>', CertifiedExperienceView.as_view(), name = 'certified_experience'),
]