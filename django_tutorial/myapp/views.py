from django.shortcuts import render

# Create your views here.

def index(request):
    print("estoy renderizando un index")
    return render(request, 'myapp/index.html', {})

def index2(request):
    return render(request, 'myapp/index_2.html', {})
