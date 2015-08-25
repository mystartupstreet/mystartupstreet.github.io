from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactUs

# Create your views here.
def index(request):
    return render(request, 'stanley/theme/index.html')

def storyoftheweek(request):
    return render(request, 'stanley/theme/storyoftheweek.html')

def books(request):
    return render(request, 'stanley/theme/books.html')

def videos(request):
    return render(request, 'stanley/theme/videos.html')

def courses(request):
    return render(request, 'stanley/theme/courses.html')

def blog(request):
    return render(request, 'stanley/theme/blog.html')

def contact(request):
    form = ContactUs
    return render(request, 'stanley/theme/contact.html', {'form': form})

def thanks(request):
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            recipient = ['shubhnkar123988@nitp.ac.in']
            #send_mail(subject, message, email, recipient)
            return render(request, 'stanley/theme/thanks.html', {'name': name})
    else:
        form = ContactUs

    return render(request, 'stanley/theme/contact.html', {'form': form})
