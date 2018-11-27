from django.db import models
from neomodel import (StructuredNode, StringProperty, IntegerProperty,
    RelationshipTo, RelationshipFrom)

class Profil(StructuredNode):
	nom = StringProperty()
	redirige = RelationshipFrom('Page','IS_FROM')

class Page(StructuredNode):
	url = StringProperty()

P1 = Profil(nom="P1").save()
P2 = Profil(nom="P2").save()
P3 = Profil(nom="P3").save()
P4 = Profil(nom="P4").save()
P5 = Profil(nom="P5").save()
P6 = Profil(nom="P6").save()
P7 = Profil(nom="P7").save()

Page1 = Page(nom="ChangeAssuranceRAS").save()
Page2 = Page(nom="envisageEmprunt").save()
Page3 = Page(nom="veutEmpruntRAS").save()
Page4 = Page(nom="subiRefus").save()
Page5 = Page(nom="estPerdu").save()
Page6 = Page(nom="veutEmprunt").save()
Page7 = Page(nom="ChangeAssurance").save()

P1.redirige.connect(Page1)
P2.redirige.connect(Page2)
P3.redirige.connect(Page3)
P4.redirige.connect(Page4)
P5.redirige.connect(Page5)
P6.redirige.connect(Page6)
P7.redirige.connect(Page7)

for p in Page1.redirige.all()
    print(p.name)