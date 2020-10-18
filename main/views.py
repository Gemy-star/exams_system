from django.shortcuts import render
from exam.models import Category


def home_page(request):
    context = {"cats": Category.objects.all()}
    return render(request, 'main/home.html', context=context)
