from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label = "Prenom", max_length=30, required=False, help_text='Optionnel.')
    last_name = forms.CharField(label = "Nom", max_length=30, required=False, help_text='Optionnel.')
    email = forms.EmailField(label = "Mail", max_length=254, help_text='Requis.')
    ras = forms.BooleanField(label = "Risque Aggravé de Santé", required=False, help_text='Optionnel.')

    CHOICES=[('P1','RAS - Je veux changer d\'assurance'),
         ('P2','RAS - J\'envisage de faire un emprunt et recherche des informations'),
         ('P3','RAS - Je vais faire un emprunt'),
         ('P4','RAS - J\'ai subi de nombreux refus des banques et assurances'),
         ('P5','RAS - Je suis un peu perdu'),
         ('P6','Non RAS - Je veux faire un emprunt'),
         ('P7','Non RAS - Je veux changer d\'assurance')]

    profil = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label = "Selectionnez votre profil", help_text='Requis.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'ras', 'profil',)
