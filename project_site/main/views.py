from django.shortcuts import render
from .models import Reviews
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponseNotFound


def index(request):
    return render(request, "index.html")


def reviews(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        if request.POST.get('name') and request.POST.get('review'):
            if len(request.POST.get('review')) < 10:
                return JsonResponse({"status": 'short'})
            new_review = Reviews()
            new_review.name = request.POST.get('name')
            new_review.review = request.POST.get("review")
            new_review.save()
            return JsonResponse({"status": 'success'})
        else:
            return JsonResponse({"status": 'fail'})

    mas = []
    for review in Reviews.objects.all():
        mas.append({'name': review.name, 'review': review.review, 'date': str((review.date + timedelta(hours=3)).strftime("%d.%m.%Y %H:%M"))})
    return render(request, 'reviews.html', {'reviews': mas})


def contacts(request):
    return render(request, 'contacts.html')
