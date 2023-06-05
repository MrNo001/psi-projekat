from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from offer.models import Offer, Picture
from search import views as v
from django.http import HttpResponse


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
def dashboard(request):
    offers = Offer.objects.filter(created_by=request.user)

    packed = []
    for offer in offers:
        packed.append({
            'offer': offer,
            'image': Picture.objects.filter(offer=offer)[0]
        })

    return render(request, 'account/dashboard.html', {
        'offers': packed,
    })

@login_required
def editProfile(request):
    
    return HttpResponse("TODO")


def logoutuser(request):
    logout(request)
    return v.index(request)
