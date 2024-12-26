from django.shortcuts import render




def skills(request):
    context = {'skills': 'active'}
    return render(request, 'education/skills.html', context)