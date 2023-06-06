from django.shortcuts import render,get_object_or_404,redirect
from offer.models import Offer
from company.forms import RateForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from account.models import User
from .models import Review


def plac(request,firm_name):

            user = User.objects.get(username=firm_name)
            reviews = Review.objects.filter(firm=user)

            myReviewsPacked = []
            for review in reviews:
                myReviewsPacked.append({
                    'review': review,
                })


            return render(request,'company/plac.html',{'firm_name':firm_name,'reviews':myReviewsPacked})




def rate(request, firm_name):
        
        firm=User.objects.get(username=firm_name)
        user = request.user
        

        if request.method == 'POST':
            form = RateForm(request.POST)
            if form.is_valid():
                rate = form.save(commit=False)
                rate.user = user
                rate.firm = firm
                rate.save()
                return HttpResponseRedirect(reverse('company:plac', args=[firm]))
        else:
            form = RateForm()

        template = loader.get_template('company/rate.html')

        context = {
            'form': form, 
            'firm_name':firm_name
        }

        return HttpResponse(template.render(context, request))



# def reviews(request, firm_name):
        
       

#         template = loader.get_template('company/company_review.html')

#         return HttpResponse(template.render(context, request))


# def plac(request,name):

#     return render(request, 'offer/form2.html', {
#         'form1': form1,
#         'form2': form2,
#         'title': 'Kreiranje oglasa',
#     })