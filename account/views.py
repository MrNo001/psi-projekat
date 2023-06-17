from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from offer.models import Offer, Picture
from search import views as v
from django.http import HttpResponse
from django.views.decorators.cache import cache_control

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/', permanent=True)
    else:
        form = SignupForm()

    return render(request, 'account/signup.html', {
        'form': form
    })


@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    
    myOffers = Offer.objects.filter(created_by=request.user)
    myOffersPacked = []
    for offer in myOffers:
        myOffersPacked.append({
            'offer': offer,
            'image': Picture.objects.filter(offer=offer)[0]
        })

    trackedOffers = Offer.objects.filter(subscribers=request.user)
    trackedOffersPacked = []
    for offer in trackedOffers:
        trackedOffersPacked.append({
            'offer': offer,
            'image': Picture.objects.filter(offer=offer)[0]
        })

    return render(request, 'account/dashboard_v2.html', {
        'myOffers': myOffersPacked,
        'trackedOffers': trackedOffersPacked,
    })

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editProfile(request):
    
    # return HttpResponse("TODO")

    return render(request, 'account/edit.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutuser(request):
    logout(request)
    return v.index(request)


