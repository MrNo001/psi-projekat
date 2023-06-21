from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from offer.models import Offer,Picture
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from django.core.exceptions import PermissionDenied

def admin_required(view_func):
    def wrapper_view(request, *args, **kwargs):
        if not request.user.tip == "A":
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    
    def check_admin(user):
        if not user.tip == "A":
            raise PermissionDenied
        return True

    return user_passes_test(check_admin)(view_func)

@login_required
@admin_required
def panel(request):

    ReportedOffers = Offer.objects.filter(reported = True)
    ReportedOffersPacked = []
    for offer in ReportedOffers:
        ReportedOffersPacked.append({
            'offer': offer,
            'image': Picture.objects.filter(offer=offer)[0],
            'which': 'reported',
        })

    return render(request, 'moderator/panel.html', {
        'ReportedOffers': ReportedOffersPacked
    })


@login_required
def report(request):
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
@admin_required
def resolve(request):
    if request.method == 'POST' and 'offer_id' in request.POST:
        offer_id = request.POST['offer_id']
        try:
            offer = Offer.objects.get(id=offer_id)
            offer.reported = False
            offer.save()
            return JsonResponse({'success': True})
        except Offer.DoesNotExist:
            pass
    return JsonResponse({'success': False})
