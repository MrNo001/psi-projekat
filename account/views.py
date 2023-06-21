from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from offer.models import Offer, Picture
from search import views as v
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
from django.contrib import messages
from .models import User
from django.contrib.auth import login, authenticate
from django.urls import reverse

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
            'image': Picture.objects.filter(offer=offer)[0],
            'which': "mine",
        })

    trackedOffers = Offer.objects.filter(subscribers=request.user)
    trackedOffersPacked = []
    for offer in trackedOffers:
        trackedOffersPacked.append({
            'offer': offer,
            'image': Picture.objects.filter(offer=offer)[0],
            'which': "followed",
        })

    return render(request, 'account/dashboard.html', {
        'myOffers': myOffersPacked,
        'trackedOffers': trackedOffersPacked,
    })

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def editProfile(request):
    currentuser=User.objects.get(id=request.user.id)
    
    form = SignupForm(request.POST or None,instance=currentuser)
    if form.is_valid():
        form.save()
        messages.success(request, 'Job Posted Successfully')
        login(request,currentuser)
        return redirect('account:dashboard')

    return render(request, 'account/edit.html',{'form':form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutuser(request):
    logout(request)
    return redirect(reverse("search:home"))


