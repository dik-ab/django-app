from django.db import models

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

    class Meta:
        db_table = 'experiences'

    
    def __str__(self):
        return self.name
