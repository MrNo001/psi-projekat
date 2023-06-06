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
    make = request.GET.get('make','')
    model = request.GET.get('model','')
    yearStart = request.GET.get('yearStart','')
    yearEnd = request.GET.get('yearEnd','')

    offers = Offer.objects.filter()


    if query:
        offers = offers.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if make:
        offers = offers.filter(make__icontains=make)
    if model:
        offers = offers.filter(model__icontains=model)
    if yearStart:
        offers = offers.filter(year__gte=yearStart)
    if yearEnd:
        offers = offers.filter(year__lte=yearEnd)
    

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
        'make':make,
        'model':model,
        'yearStart':yearStart,
        'yearEnd':yearEnd,   
    })

def about(request):

    return HttpResponse("O nama")
