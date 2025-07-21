from django.shortcuts import render


# Create your views here.

def photography(request):
    return render(request, 'photography.html')
