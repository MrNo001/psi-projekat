from django.shortcuts import render
from django.http import HttpResponse
from offer.models import Offer,Picture

def panel(request):

    ReportedOffers = Offer.objects.filter(reported = True)
    ReportedOffersPacked = []
    for offer in ReportedOffers:
        ReportedOffersPacked.append({
            'offer': offer,
            'image': Picture.objects.filter(offer=offer)[0]
        })

    return render(request, 'moderator/panel.html', {
        'ReportedOffers': ReportedOffersPacked
    })

