from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from main.forms import RegisterForm
from neomodel import (StructuredNode, StringProperty, IntegerProperty,
    RelationshipTo, RelationshipFrom)
from neomodel import db, clear_neo4j_database
from .models import Profil, Page
from django.shortcuts import redirect
from main.models import ContenusPage

def index(request):
    value = ContenusPage.create(1, "test")
    value.save()
    return render(request, 'main/index.html', {})

def connexion(request):
    username = request.POST.get('username');
    password = request.POST.get('password');
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active :
        login(request, user)
        return redirect('conseils')

    if username is None and password is None:
        return render(request, 'main/connexion.html')
    else:
        return render(request, 'main/connexion.html', {"message":"Identifiants invalides"})

def enregistrement(request):
    if(request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.save()
            login(request, user)
            return redirect('conseils')
    else:
        form = RegisterForm()
    return render(request, 'main/enregistrement.html', {'form': form})

def deconnexion(request):
    logout(request)
    return render(request, 'main/deconnexion.html')

def resetDatabase(request):

    if 1:
        clear_neo4j_database(db)

        P1 = Profil(nom="P1").save()
        P2 = Profil(nom="P2").save()
        P3 = Profil(nom="P3").save()
        P4 = Profil(nom="P4").save()
        P5 = Profil(nom="P5").save()
        P6 = Profil(nom="P6").save()
        P7 = Profil(nom="P7").save()

        Page1 = Page(url="changeAssuranceRAS").save()
        Page2 = Page(url="envisageEmprunt").save()
        Page3 = Page(url="veutEmpruntRAS").save()
        Page4 = Page(url="subiRefus").save()
        Page5 = Page(url="estPerdu").save()
        Page6 = Page(url="veutEmprunt").save()
        Page7 = Page(url="changeAssurance").save()

        P1.redirige.connect(Page1)
        P2.redirige.connect(Page2)
        P3.redirige.connect(Page3)
        P4.redirige.connect(Page4)
        P5.redirige.connect(Page5)
        P6.redirige.connect(Page6)
        P7.redirige.connect(Page7)

        reponse = "Reset effectué"

    return render(request, 'main/test.html', {'profils' : Profil.nodes.all(), 'pages' : Page.nodes.all(), 'reponse' : reponse})

def conseils(request):

    nomProfilRecuMYSQL = "P1" 
    if request.user.is_authenticated:
        if hasattr(request.user, 'profil'):
            nomProfilRecuMYSQL = request.user.profil
        
    ProfilRecuMYSQL = Profil.nodes.get(nom=nomProfilRecuMYSQL)
    reponse = "index"

    for unePage in Page.nodes.all():
        if ProfilRecuMYSQL.redirige.is_connected(unePage):
            reponse = unePage.url
    return render(request, 'main/'+reponse+'.html');
