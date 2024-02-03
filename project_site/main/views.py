from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def reviews(request):
    return render(request, 'reviews.html')


def contacts(request):
    return render(request, 'contacts.html')
