from django.shortcuts import render



def services(request):
    context = {'services': 'active'}
    return render(request, 'services/services.html', context)