from django.shortcuts import render

def home_view(request):
    context = {"page": "home"}
    return render(request, 'siteinfo/home.html', context)

def info_view(request):
    context = {"page": "info"}
    return render(request, 'siteinfo/info.html', context)