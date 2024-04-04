from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def homepage(request):    
    return render(request, "login_page/index.html")

@login_required(login_url="/login/")
def plataforma(request):
    if request.method == "GET":
        return render(request, "login_page/plataforma.html", )

def login(request):
    if request.method == "GET" and request.user.is_authenticated:
        return redirect("index")
    elif request.method == "GET":
        return render(request, "login_page/login.html", )
    else:
        username = request.POST.get("username")
        senha = request.POST.get("password")
        user = authenticate(username=username, password=senha)

        if user:
            login_django(request,user)
            return redirect("index")
        else:
            return HttpResponse("Email ou senha inválido")