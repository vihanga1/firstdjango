from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView
from django.http import HttpResponse
from .models import Student
from . import forms


# Create your views here.
def regForm(request):
    form = forms.SignUp()
    if request.method == "POST":
        form = forms.SignUp(request.POST)
        html = "We have recieved this form again!"
        if form.is_valid():
            html = html + " Form is Valid!"
    else:
        html = "Welcome for first Time!"
    return render(request, 'signup.html', {'html': html, 'form': form})
