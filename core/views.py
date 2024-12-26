from django.shortcuts import render



def home_page(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)


def contact(request):
    context = {'contact': 'active'}
    return render(request, 'core/contact.html', context)