from django.db import models
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
    title = models.CharField(max_length = 50)
    how_to_study = models.CharField(max_length = 100)
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
