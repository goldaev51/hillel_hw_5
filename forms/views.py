import math

from django.shortcuts import render

from .forms import TriangleForm


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
