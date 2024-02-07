from django.shortcuts import render
from .models import Reviews
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponseNotFound
from django.core.mail import send_mail, EmailMessage


def index(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        if request.POST.get('name') and request.POST.get('number'):
            email = EmailMessage('Новая заявка на сайте "Содействие и защита"',f"Имя: {request.POST.get('name')}\nНомер телефона: {request.POST.get('number')}",  "sunclub.stor@gmail.com",
                      ["cazonovp@mail.ru"])
            email.send()
            return JsonResponse({"status": 'success'})
        else:
            return JsonResponse({"status": 'fail'})
    return render(request, "index.html")


def reviews(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        if request.POST.get('name') and request.POST.get('review'):
            if len(request.POST.get('review')) < 10:
                return JsonResponse({"status": 'short'})
            email = EmailMessage('Новый отзыв на сайте "Содействие и защита"',f"Имя: {request.POST.get('name')}\nОтзыв: {request.POST.get('review')}",  "sunclub.stor@gmail.com",
                      ["cazonovp@mail.ru"])
            email.send()
            # new_review = Reviews()
            # new_review.name = request.POST.get('name')
            # new_review.review = request.POST.get("review")
            # new_review.save()
            return JsonResponse({"status": 'success'})
        else:
            return JsonResponse({"status": 'fail'})

    mas = []
    for review in Reviews.objects.all():
        mas.append({'name': review.name, 'review': review.review, 'date': str((review.date + timedelta(hours=3)).strftime("%d.%m.%Y %H:%M"))})
    return render(request, 'reviews.html', {'reviews': mas})


def contacts(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        if request.POST.get('name') and request.POST.get('number') and request.POST.get('email') and request.POST.get('message'):
            if request.POST.get('checked') == 'true':
                email = EmailMessage('Новая заявка на сайте "Содействие и защита"',f"Имя: {request.POST.get('name')}\nНомер телефона: {request.POST.get('number')}\nEmail: {request.POST.get('email')}\nСообщение: {request.POST.get('message')}",
                           "sunclub.stor@gmail.com",
                          ["cazonovp@mail.ru"])
                email.send()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'not_checked'})
        else:
            return JsonResponse({"status": 'fail'})
    return render(request, 'contacts.html')


def personal_data(request):
    return render(request, 'personal_data.html')
