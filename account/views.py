from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import SignupForm
from offer.models import Offer
from search import views as v


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/account/login/', permanent=True)
    else:
        form = SignupForm()

    return render(request, 'account/signup.html', {
        'form': form
    })


@login_required

def dashboard(request):
    offers = Offer.objects.filter(created_by=request.user)

    return render(request, 'account/dashboard.html', {
        'offers': offers,
    })


def logoutuser(request):
    logout(request)
    return v.index(request)
    