from django.urls import path
from .views import (
    CertificationListView, ExperienceListView,
    ExperienceDetailView, ExperienceFormView,ThanksView
)

app_name = 'certifications'

urlpatterns = [
    path('', CertificationListView.as_view(), name = 'certification_list'),
    path('合格体験記一覧/<int:pk>', ExperienceListView.as_view(), name = '合格体験記一覧'),
    path('pass/<int:pk>', ExperienceDetailView.as_view(), name = 'pass'),
    path('write/', ExperienceFormView.as_view(), name = 'write'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
]
