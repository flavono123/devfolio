from django.conf import settings
from django.forms.models import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView

import pickle

from .forms import ResumeForm, CareerForm, EducationForm, AwardForm, LinkForm
from .models import Resume, Career, Education, Award, Link


def resume_detail(request, id):
    resume = get_object_or_404(Resume, id=id)
    if request.user != resume.user:
        return HttpResponse('No Permission')

    return render(request, 'resume/detail.html', {
        'resume': resume,
    })

def resume_form(request):
    # Prepare formsets
    CareerFormSet = modelformset_factory(Career, 
        form=CareerForm,
        max_num=5, 
        validate_max=True,
        extra=0
    )

    EducationFormSet = modelformset_factory(Education, 
        form=EducationForm,
        max_num=5, 
        validate_max=True,
        extra=0
    )

    AwardFormSet = modelformset_factory(Award, 
        form=AwardForm,
        max_num=5, 
        validate_max=True,
        extra=0
    )

    if request.method == 'POST':
        # Resume POST form
        form = ResumeForm(request.POST)

        # Career POST formset
        career_formset = CareerFormSet(request.POST, 
            prefix='career', 
            queryset=Career.objects.none()
        )

        # Education POST formset
        education_formset = EducationFormSet(request.POST, 
            prefix='education', 
            queryset=Education.objects.none()
        )
        
        # Award POST formset
        award_formset = AwardFormSet(request.POST,
            prefix='award',
            queryset=Award.objects.none()
        )
        
        # Link POST form
        link_form = LinkForm(request.POST)

        if form.is_valid() and career_formset.is_valid() and education_formset.is_valid() and award_formset.is_valid() and link_form.is_valid():
            # save Resume
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            # save Career
            careers = career_formset.save(commit=False)
            for career in careers:
                career.resume = resume
                career.save()

            # save Education 
            educations = education_formset.save(commit=False)
            for education in educations:
                education.resume = resume
                education.save()

            # save Award 
            awards = award_formset.save(commit=False)
            for award in awards:
                award.resume = resume
                award.save()

            # save Link
            link = link_form.save(commit=False)
            link.resume = resume
            link.save()

            return redirect('resume:list')
    else:
        # Resume GET form
        form = ResumeForm(initial={
            'email': request.user.email,
        })

        # Career GET form
        career_formset = CareerFormSet(prefix='career',
            queryset=Career.objects.none()
        )

        # Education GET form
        education_formset = EducationFormSet(prefix='education',
            queryset=Education.objects.none()
        )

        # Award GET form
        award_formset = AwardFormSet(prefix='award',
            queryset=Award.objects.none()
        )

        # Link GET form
        link_form = LinkForm()

    # Load devicon name list from the pickle file
    pkl_file = settings.ROOT('devfolio', 'static', 'devicon_name_list.pkl')
    with open(pkl_file, 'rb') as f:
        devicon_name_list = pickle.load(f)

    return render(request, 'resume/form.html', {
        'form': form,
        'career_formset': career_formset,
        'education_formset': education_formset,
        'award_formset': award_formset,
        'link_form': link_form,
        'first_row_field_list': ['until', 'since', 'at', 'currently_employed', 'currently_attending'],
        'date_field_list': ['until', 'since', 'at'],
        'devicon_name_list': devicon_name_list,
    })

def resume_list(request):
    resume_list = Resume.objects.filter(user=request.user.id)
    return render(request, 'resume/list.html', {
        'resume_list': resume_list,
    })
