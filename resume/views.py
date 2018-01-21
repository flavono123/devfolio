from django.shortcuts import render, redirect
from django.conf import settings

import json

from .forms import ResumeForm
from .models import Resume


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
        'resume_list': resume_list,
        'svg_dict': svg_dict,
    })

def list(request):
    resume_list = Resume.objects.all()
    return render(request, 'resume/list.html', {
        'resume_list': resume_list,
    })
