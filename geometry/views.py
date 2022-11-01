from django.shortcuts import render
from .forms import HypoForm


def triangle(request):
    form = HypoForm()
    if 'submit' in request.GET:
        form = HypoForm(request.GET)
        if form.is_valid():
            gip = pow(int(form.cleaned_data['catet']), 2) + pow(int(form.cleaned_data['catet2']), 2)
            return render(request, 'hypotenuse.html', {'form': form, 'gip': gip})
    return render(request, 'hypotenuse.html', {'form': form})
