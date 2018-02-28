from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse

import io
from PIL import Image
import Identicon

from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

def identicon(request):
    identicon = Identicon.render(request.user.email)
    image = Image.open(io.BytesIO(identicon))
    response = HttpResponse(content_type='image/png')
    image.save(response, format="PNG")
    return response



