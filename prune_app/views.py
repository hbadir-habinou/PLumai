from django.shortcuts import render

def index(request):
    return render(request, 'prune_app/index.html')

def a_propos(request):
    return render(request, 'prune_app/a_propos.html')

def contact(request):
    return render(request, 'prune_app/contact.html')

def nos_services(request):
    return render(request, 'prune_app/nos_services.html')

def login(request):
    return render(request, 'prune_app/login.html')

def signin(request):
    return render(request, 'prune_app/signin.html')

def prediction_plum(request):
    return render(request, 'prune_app/prediction_plum.html')