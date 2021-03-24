from django.contrib import admin
from .models import (
    Certifications, Experiences,
)

admin.site.register(
    [Certifications, Experiences]
)
