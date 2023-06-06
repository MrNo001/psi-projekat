from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewOfferForm, EditOfferForm, FileFieldForm
from .models import Offer, Picture
from django.contrib import messages



def details(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    related_offers = Offer.objects.filter().exclude(pk=pk)[0:5]
    images = Picture.objects.filter(offer=pk)

    
    if request.method == 'POST':
        offer.reported = True
        offer.save()
        messages.info(request, 'Add successfuly reported')
       

    packed = []
    for offer in related_offers:
        packed.append({
            'offer': offer,
            'image': Picture.objects.filter(offer=offer)[0]
        })

    return render(request, 'offer/details.html', {
        'offer': offer,
        'images': images,
        'range': range(len(images)),
        'related_offers': packed
    })

@login_required
def new(request):
    if request.method == 'POST':
        form1 = NewOfferForm(request.POST, request.FILES)
        form2 = FileFieldForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            offer = form1.save(commit=False)
            # offer = Offer()
            offer.created_by = request.user
            offer.save()

            for img in request.FILES.getlist('file_field'):
                picture = Picture()
                picture.image = img
                picture.offer = offer
                picture.save()


            return redirect('offer:details', pk=offer.id)
    else:
        form1 = NewOfferForm()
        form2 = FileFieldForm()

    return render(request, 'offer/form.html', {
        'form1': form1,
        'form2': form2,
        'title': 'Kreiranje oglasa',
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
        'title': 'Izmena oglasa',
    })

@login_required

def delete(request, pk):
    offer = get_object_or_404(Offer, pk=pk)#created_by=request.user
    offer.delete()
    return redirect('/')
