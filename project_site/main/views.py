from django.shortcuts import render
from .models import Reviews


def index(request):
    return render(request, "index.html")


def reviews(request):
    mas = []
    for review in Reviews.objects.all():
        mas.append({'name': review.name, 'review': review.review, 'date': str(review.date.strftime("%d.%m.%Y %H:%M"))})
    return render(request, 'reviews.html', {'reviews': mas})


def contacts(request):
    return render(request, 'contacts.html')
