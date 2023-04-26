from django.shortcuts import render

# Create your views here.

from .forms import FormContactForm

def showform(request):
    form=FormContactForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, 'ContactForm.html')