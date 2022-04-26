from django.shortcuts import render

# Create your views here.


def home(request):
    x = {
        "x":10
    }
    return render(request, 'home.html', x)
