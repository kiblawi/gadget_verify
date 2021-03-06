from django.db import models
from datetime import datetime

# Create your models here.

class Query(models.Model):
    name = models.CharField(max_length=100,primary_key = True)

    def __unicode__(self):
        return self.name


"""Abstract table has a Name field used as a the primary key"""
class Abstract(models.Model):
    pmid = models.IntegerField(primary_key=True)
    link = models.URLField()
    author = models.TextField()
    title = models.TextField()


    def __unicode__(self):
        return self.title

"""Gene table has name as a primary key and has a many to many relationship
with abstracts. A gene may appear in many abstracts, and a abstract may contain
many genes"""
class Gene(models.Model):
    name = models.CharField(max_length=200)
    entrez = models.IntegerField()
    true_relevance = models.BooleanField(default=True)
    symbol = models.CharField(max_length=200)
    synonyms = models.TextField()
    abstracts = models.ManyToManyField(Abstract)
    query = models.ForeignKey(Query)

    def __unicode__(self):
        return self.name

"""Surveyor is the expert who is going to perform validation for us. 
Primary key is a autogenerated ID that django implements automatically.
Surveyor will verify many genes, and a gene may be verified by many 
surveyors so it is a many to many relationship, that acts through the choices
table"""
class Surveyor(models.Model):
    name = models.CharField(max_length=100)
    genes = models.ManyToManyField(Gene, through = 'Choice')
    query = models.ForeignKey(Query)

    def __unicode__(self):
        return self.name

"""Choices is a relationship table that identifies whether the Surveyor has
chosen a specific gene as relevant"""
class Choice(models.Model):
    surveyor = models.ForeignKey(Surveyor)
    gene = models.ForeignKey(Gene)
    relevant = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True,blank=True)

    @property
    def getGene(self):
        return Gene.objects.get(name=self.gene,query=self.surveyor.query)

    def __unicode__(self):
        return unicode(self.id)



