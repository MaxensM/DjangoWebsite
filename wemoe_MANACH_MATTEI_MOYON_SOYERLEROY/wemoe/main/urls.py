from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('connexion', views.connexion, name='connexion'),
    path('enregistrement', views.enregistrement, name='enregistrement'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
    path('test', views.resetDatabase, name="test"),
    path('conseils', views.conseils, name="conseils"),
    path('', views.index, name='index'),

    path('changeAssuranceRAS', TemplateView.as_view(template_name='main/changeAssuranceRAS.html'), name='changeAssuranceRAS'),
    path('changeAssurance', TemplateView.as_view(template_name='main/changeAssurance.html'), name='changeAssurance'),
    path('envisageEmprunt', TemplateView.as_view(template_name='main/envisageEmprunt.html'), name='envisageEmprunt'),
    path('subiRefus', TemplateView.as_view(template_name='main/subiRefus.html'), name='subiRefus'),
    path('estPerdu', TemplateView.as_view(template_name='main/estPerdu.html'), name='estPerdu'),
    path('veutEmpruntRAS', TemplateView.as_view(template_name='main/veutEmpruntRAS.html'), name='veutEmpruntRAS'),
    path('veutEmprunt', TemplateView.as_view(template_name='main/veutEmprunt.html'), name='veutEmprunt'),
]