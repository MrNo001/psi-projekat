from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewOfferForm, EditOfferForm
from .models import Offer, Picture



def details(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    related_offers = Offer.objects.filter().exclude(pk=pk)[0:3]
    images = Picture.objects.filter(offer=pk)
    print(related_offers)
    print(images)

    return render(request, 'offer/details.html', {
        'offer': offer,
        'images': images,
        'range': range(len(images)),
        'related_offers': related_offers
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewOfferForm(request.POST, request.FILES)

        if form.is_valid():
            # offer = form.save(commit=False)
            offer = Offer()
            offer.name = form.cleaned_data['name']
            offer.created_by = request.user
            offer.price = 100
            offer.save()

            for img in request.FILES.getlist('file_field'):
                picture = Picture()
                picture.image = img
                picture.offer = offer
                picture.save()


            return redirect('offer:details', pk=offer.id)
    else:
        form = NewOfferForm()

    return render(request, 'offer/form2.html', {
        'form': form,
        'title': 'New offer',
    })

@login_required
def edit(request, pk):
    offer = get_object_or_404(Offer, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditOfferForm(request.POST, request.FILES, instance=offer)

        if form.is_valid():
            form.save()

            return redirect('offer:details', pk=offer.id)
    else:
        form = EditOfferForm(instance=offer)

    return render(request, 'offer/form.html', {
        'form': form,
        'title': 'Edit offer',
    })

@login_required

def delete(request, pk):
    offer = get_object_or_404(Offer, pk=pk, created_by=request.user)
    offer.delete()
    return redirect('/')
