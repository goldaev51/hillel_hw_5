import math

from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import PersonForm, TriangleForm
from .models import Person


class PersonListView(generic.ListView):
    model = Person
    paginate_by = 10


def person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('forms:person-info', obj.id)
    else:
        form = PersonForm()
    return render(request, 'forms/person_create.html', {'form': form})


def person_info(request, pk):
    person_data = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person_data)
        if form.is_valid():
            obj = form.save()
            return redirect('forms:person-info', obj.id)
    else:
        form = PersonForm(instance=person_data)

    return render(request, 'forms/person_info.html', {'form': form})


def triangle(request):
    hypotenuse = None
    if 'submit' in request.GET:
        form = TriangleForm(request.GET)
        if form.is_valid():
            hypotenuse = round(math.sqrt((form.cleaned_data['leg_1'] ** 2) +
                                         (form.cleaned_data['leg_2'] ** 2)), 1)
    else:
        form = TriangleForm()

    return render(request, 'forms/triangle.html', {'form': form, 'hypotenuse': hypotenuse})
