from django.test import TestCase
from django.urls import resolve, reverse
from certifications.views import (
    CertificationListView, ExperienceListView ,
    ExperienceDetailView, ExperienceFormView,
)
from certifications.models import Certifications, Experiences



class CertificationsUrlsTest(TestCase):
    
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

    def test_certification_list_url(self):
        url = resolve('/')
        self.assertEqual(url.func.view_class, CertificationListView)

    def test_experience_list_url(self):
        url = reverse('certifications:experience_list', args=[1])
        self.assertEqual(resolve(url).func.view_class, ExperienceListView)

    def test_experience_detail_url(self):
        url = reverse('certifications:experience_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, ExperienceDetailView)

    def test_experience_form_url(self):
        url = reverse('certifications:experience_form')
        self.assertEqual(resolve(url).func.view_class, ExperienceFormView)

        


