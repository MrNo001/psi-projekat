from django.shortcuts import render
from offer.models import Offer, Picture
from account.forms import SignupForm
from django.db.models import Q
from django.http import HttpResponse


def index(request):
    offers = Offer.objects.filter(is_premium=True)[0:6]

    return render(request, 'search/home.html', {
        'offers': offers
    })

def browse(request):
    query = request.GET.get('query', '')
    offers = Offer.objects.filter()

    if query:
        offers = offers.filter(Q(name__icontains=query) | Q(description__icontains=query))

    packed = []
    for offer in offers:
        packed.append({
            'offer': offer,
            'image': Picture.objects.filter(offer=offer)[0]
        })

    return render(request, 'search/browse.html', {
        'offers': packed,
        # 'images': images,
        'query': query,
    })

def about(request):

    return HttpResponse("O nama")
