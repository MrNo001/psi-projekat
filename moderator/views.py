from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from offer.models import Offer,Picture
from django.contrib.auth.decorators import login_required

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


@login_required
def report(request):




    return JsonResponse({'success': False})


@login_required
def resolve(request):
    if request.method == 'POST' and 'offer_id' in request.POST:
        if request.user.tip != "A":
            return JsonResponse({'success': False})
        offer_id = request.POST['offer_id']
        try:
            offer = Offer.objects.get(id=offer_id)
            offer.reported = False
            offer.save()
            return JsonResponse({'success': True})
        except Offer.DoesNotExist:
            pass
    return JsonResponse({'success': False})