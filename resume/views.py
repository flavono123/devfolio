from django.shortcuts import render, redirect

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
    return render(request, 'resume/index.html', {
        'form': form,
    })

def list(request):
    resume_list = Resume.objects.all()
    return render(request, 'resume/list.html', {
        'resume_list': resume_list,
    })
