from django.shortcuts import render

# Create your views here.

def django_mtv(request):
    return render(request, 'main/django_mtv.html')

def free_page(request):
    return render(request, 'main/free_page.html')