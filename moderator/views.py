from django.shortcuts import render
from django.http import HttpResponse
from offer.models import Offer,Picture
from django.http import JsonResponse

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


def report_ad(request):
    if request.method == 'POST' and 'offer_id' in request.POST:
        offer_id = request.POST['offer_id']
        try:
            offer = Offer.objects.get(id=offer_id)
            offer.reported = True
            offer.save()
            return JsonResponse({'success': True})
        except Offer.DoesNotExist:
            pass
    return JsonResponse({'success': False})

def follow_ad(request):
    if request.method == 'POST' and 'offer_id' in request.POST:
        offer_id = request.POST['offer_id']
        try:
            offer = Offer.objects.get(id=offer_id)
            offer.subscribers.add(request.user)
            offer.save()
            return JsonResponse({'success': True})
        except Offer.DoesNotExist:
            pass
    return JsonResponse({'success': False})

