from django.shortcuts import render
from offer.models import Offer
from account.forms import SignupForm
from django.db.models import Q


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

    return render(request, 'search/browse.html', {
        'offers': offers,
        'query': query,
    })
