from django.db import models
from django.utils import timezone
from django.contrib.sessions.models import Session

#from accounts import Users

class Certifications(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        db_table = 'certifications'

    def __str__(self):
        return self.name


class Experiences(models.Model):
    certification = models.ForeignKey(
        Certifications, on_delete = models.CASCADE
    )
    score = models.CharField(max_length=50, default='')
    timestamp = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length = 50)
    how_to_study = models.CharField(max_length = 100)
    how_to_study_site = models.CharField(max_length = 100, default='')
    study_time = models.CharField(max_length = 30)
    url = models.URLField(max_length = 200, null=True, blank=True)
    description = models.TextField(default = '', max_length = 10000)
    # user = models.ForeignKey(
    #     Users, on_delete = models.CASCADE
    # )

    class Meta:
        db_table = 'experiences'

    
    def __str__(self):
        return self.title




