from django.shortcuts import render

# Create your views here.

def index(request):
    print("estoy renderizando un index")
    return render(request, 'myapp/index.html', {})

def install(request):
    return render(request, 'myapp/install.html', {})

def models(request):
    return render(request, 'myapp/models.html', {})

def index3(request):
    return render(request, 'myapp/index_2.html', {})
