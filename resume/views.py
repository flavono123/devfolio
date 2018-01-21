from django.shortcuts import render

from .forms import ResumeForm


def index_page(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = ResumeForm()
    return render(request, 'resume/index.html', {
            'form': form,
        })
