from django.db import models
from neomodel import StructuredNode, StringProperty, RelationshipFrom
from neomodel import db, clear_neo4j_database

class Page(StructuredNode):
	url = StringProperty()

class Profil(StructuredNode):
    nom = StringProperty(unique_index=True)
    redirige = RelationshipFrom('Page','IS_FROM')

class ContenusPage(models.Model):
    id = models.IntegerField(primary_key=True)
    texte = models.TextField(max_length=4096)

    @classmethod
    def create(cls, id, texte):
        contenus = cls(id=id, texte=texte)
        contenus.save()
        return contenus

    class Meta:
        app_label = "mongo"
