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
    score = models.CharField(max_length=50, default='',null=True,blank=True)
    common_test_score = models.CharField(max_length=50,null=True,blank=True)
    timestamp = models.DateTimeField(default = timezone.now)
    title = models.CharField(max_length = 50)
    予備校 = models.CharField(max_length=10, default='')
    recommend_class = models.TextField(max_length=1000, default='',null=True,blank=True)
    how_to_study = models.TextField(max_length = 100,null=True,blank=True)
    how_to_study_site = models.CharField(max_length = 100, default='',null=True,blank=True)
    study_method = models.TextField(max_length=10000, default='')
    advices = models.TextField(max_length=10000,null=True,blank=True)
    study_time = models.CharField(max_length = 30, null=True, blank=True)
    url = models.URLField(max_length = 200, null=True, blank=True)
    description = models.TextField(default = '', max_length = 10000, null=True, blank=True)
    # user = models.ForeignKey(
    #     Users, on_delete = models.CASCADE
    # )
    motivation = models.TextField(default = '', max_length=1000,null=True,blank=True)
    faculty = models.CharField(default='',max_length=1000)


    class Meta:
        db_table = 'experiences'

    
    def __str__(self):
        return self.title




