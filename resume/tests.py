from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils import timezone

from datetime import timedelta

from .views import index_page
from .models import Resume


class IndexViewTest(TestCase):
    
    def test_app_root_resolves_index_page(self):
        index = resolve('/resume/')
        self.assertEqual(index.func, index_page)

    def test_index_page_render_correct_html(self):
        request = HttpRequest()
        response = index_page(request)
        expected_html = render_to_string('resume/index.html')

        self.assertEqual(expected_html, response.content.decode())


class ResumeModelTest(TestCase):

    def test_saving_resumes(self):
        first_resume = Resume(name='에잇퍼센트', 
                              base_info='홍한석\n010-6434-3473\nflavono123@gmail.com')
        first_resume.save()
        second_resume = Resume(name='아테나스랩', 
                                    base_info='홍한석\n010-6434-3473\nflavono123@gmail.com')
        second_resume.save()
        
        # All resume is saved?
        saved_resumes = Resume.objects.all()

        self.assertEqual(saved_resumes.count(), 2)

        # Each resume is saved?
        first_saved_resume = saved_resumes[0]
        second_saved_resume = saved_resumes[1]

        self.assertEqual(first_saved_resume, first_resume)
        self.assertEqual(second_saved_resume, second_resume)


    def _test_saving_each_field_of_resume_right(self):
        test_resume = Resume(name='테스트', 
                             base_info='abc')
        test_resume_created_at = timezone.now() # Almost!
        #saved_resume = Resume.objects.get(base_info='abc')
        saved_resume = Resume.objects.get(name='테스트',
                                          base_info='abc')
        
        # Resume's created time is correct?
        self.assertAlmostEqual(test_resume_created_at, 
                               saved_resume.created_at,
                               delta=timedelta(seconds=2))


    def test_resumes_print_its_name(self):
        resume = Resume(name='테스트할 이름', base_info='abc')

        # Resume prints its name correct? 
        self.assertEqual(str(resume), '테스트할 이름')
