from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    print("estoy renderizando un index")
    return render(request, 'myapp/index.html', {})

def install(request):
    print('estoy llamado a install')

    return render(request, 'myapp/install.html', {})

def models(request):
    print('estoy llamado a models')
    # return redirect('install')
    return render(request, 'myapp/models.html', {})

def urls(request):
    return render(request, 'myapp/urls.html', {})
    
def views(request):
    return render(request, 'myapp/views.html', {})

def templates(request):
    return render(request, 'myapp/templates.html', {})

