from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import NewOfferForm, EditOfferForm, FileFieldForm
from .models import Offer, Picture
from django.contrib import messages



def details(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    related_offers = Offer.objects.filter(make=offer.make,model=offer.model).exclude(pk=pk)[0:5]
    images = Picture.objects.filter(offer=pk)

    
    if request.method == 'POST':
        offer.reported = True
        offer.save()
        messages.info(request, 'Add successfuly reported')

    packed = []
    for rel_offer in related_offers:
        packed.append({
            'offer': rel_offer,
            'image': Picture.objects.filter(offer=rel_offer)[0]
        })

    return render(request, 'offer/offer.html', {
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

    return render(request, 'offer/new.html', {
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

    return render(request, 'offer/edit.html', {
        'form': form,
        'title': 'Izmena oglasa',
    })

@login_required
def delete(request, pk):
    offer = get_object_or_404(Offer, pk=pk)#created_by=request.user
    offer.delete()
    return redirect('/profil/')

@login_required
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

@login_required
def follow(request, pk):
    if request.method == 'POST' and 'offer_id' in request.POST:
        offer = get_object_or_404(Offer, pk=pk)
        offer_id = request.POST['offer_id']
        try:
            offer = Offer.objects.get(id=offer_id)
            offer.subscribers.add(request.user)
            offer.save()
            return JsonResponse({'success': True})
        except Offer.DoesNotExist:
            pass
    return JsonResponse({'success': False})


@login_required
def unfollow(request, pk):
    pass

