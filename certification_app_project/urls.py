
from django.contrib import admin
from . import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('certifications.urls'))
]
