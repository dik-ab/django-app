from django.test import TestCase
from certifications.models import Certifications, Experiences



class CertificationsModelTests(TestCase):

    def setUp(self):

        self.certification = certification = Certifications.objects.create(
            name = 'test'
        )
        self.certification.save()
        self.experience = Experiences.objects.create(
            certification = certification,
            title = 'title_test',
            how_to_study = 'how_to_test',
            study_time = '2hour',
            url = 'https://test.com',
            description = 'description_test'
        )
        self.experience.save()

    def test_certification_is_not_empty(self):
        certification = self.certification
        certification.save()
        saved_certification = Certifications.objects.all()
        self.assertEqual(saved_certification.count(), 1)    

    def test_experience_is_not_empty(self):
        experience = self.experience
        experience.save()
        saved_experience = Experiences.objects.all()
        self.assertEqual(saved_experience.count(), 1)    



