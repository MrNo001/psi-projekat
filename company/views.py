from django.shortcuts import render



def plac(request,name):
    return render(request,'company/plac.html',{'name':"neko ime"})


# def plac(request,name):

#     return render(request, 'offer/form2.html', {
#         'form1': form1,
#         'form2': form2,
#         'title': 'Kreiranje oglasa',
#     })