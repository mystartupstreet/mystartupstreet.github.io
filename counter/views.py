from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import LetMeKnow

def counter(request):
    form = LetMeKnow
    var1 = False
    return render(request, 'counter/Theme/index.html', {'form': form, 'var1': var1})

def thanks(request):
    if request.method == 'POST':
        form = LetMeKnow(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            return render(request, 'counter/Theme/index.html', {'var1': True})

        return HttpResponseRedirect('/')

