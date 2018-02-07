from django.conf import settings
from django.forms.models import modelformset_factory
from django.shortcuts import render, redirect

import json

from .forms import ResumeForm, CareerForm, EducationForm, AwardForm, LinkForm
from .models import Resume, Career


def index_page(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            return redirect('resume:list')
    else:
        form = ResumeForm()
    
    svg_json_path = settings.ROOT('devfolio', 'static', 'svg_codes.json')
    with open(svg_json_path, 'r') as f:
        svg_dict = json.load(f)
    resume_list = Resume.objects.all()

    return render(request, 'resume/index.html', {
        'form': form,
        'svg_dict': svg_dict,
    })

def resume_list(request):
    resume_list = Resume.objects.filter(user=request.user.id)
    return render(request, 'resume/list.html', {
        'resume_list': resume_list,
    })


def career_form(request):
    CareerFormSet = modelformset_factory(Career, 
        form=CareerForm,
        max_num=5, 
        validate_max=True 
    )
    
    if request.method == 'POST':
        formset = CareerFormSet(request.POST, 
            prefix='career', 
            queryset=Career.objects.none()
        )
        if formset.is_valid():
            formset.save()
            return redirect('resume:index')
    else:
        formset = CareerFormSet(prefix='career',
            queryset=Career.objects.none()
        )

    return render(request, 'resume/career_form.html', {
        'formset': formset,
        'date_field_list': ['until', 'since'],
    })


def education_form(request):
    EducationFormSet = formset_factory(EducationForm, max_num=5)
    if request.method == 'POST':
        formset = EducationFormSet(request.POST, prefix='education')
        if formset.is_valid():
            formset.save()
            pass
    else:
        formset = EducationFormSet(prefix='education')
    return render(request, 'resume/education_form.html', {
        'formset': formset,
    })


def award_form(request):
    AwardFormSet = formset_factory(AwardForm, max_num=5)
    if request.method == 'POST':
        formset = AwardFormSet(request.POST, prefix='award')
        if formset.is_valid():
            formset.save()
            pass
    else:
        formset = AwardFormSet(prefix='award')
    return render(request, 'resume/award_form.html', {
        'formset': formset,
    })

    
def link_form(request):
    LinkFormSet = formset_factory(LinkForm, max_num=5)
    if request.method == 'POST':
        formset = LinkFormSet(request.POST, prefix='link')
        if formset.is_valid():
            formset.save()
            pass
    else:
        formset = LinkFormSet(prefix='link')
    return render(request, 'resume/link_form.html', {
        'formset': formset,
    })
