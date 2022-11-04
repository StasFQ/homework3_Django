from django.shortcuts import get_object_or_404, redirect, render

from .forms import HypoForm, PersonForm
from .models import Person


def triangle(request):
    form = HypoForm()
    if 'submit' in request.GET:
        form = HypoForm(request.GET)
        if form.is_valid():
            gip = pow(int(form.cleaned_data['catet']), 2) + pow(int(form.cleaned_data['catet2']), 2)
            return render(request, 'hypotenuse.html', {'form': form, 'gip': gip})
    return render(request, 'hypotenuse.html', {'form': form})


def create_person(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('geometry:create_person')
    else:
        return render(request, 'Person.html', {'form': form})
    return render(request, 'Person.html', {'form': form})


def update_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            obj = form.save()
            return redirect('geometry:update_person', obj.id)
        return render(request, 'Person_update.html', {'form': form})
    else:
        form = PersonForm(instance=person)
    return render(request, 'Person_update.html', {'form': form})
