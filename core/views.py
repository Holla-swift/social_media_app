from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        
    }
    return render(request, 'index.html', context)

def signup(request):

    if request.method == "POST":
        username = request.POST('username')
        email = request.POST('email')
        password = request.POST('password')
        password = request.POST('password2')
    else:
        return render(request, 'signup.html', context)

    context = {
        
    }
    