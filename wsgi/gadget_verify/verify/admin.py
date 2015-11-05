from django.contrib import admin

from .models import Surveyor,Choice,Abstract,Gene
# Register your models here.

def surveyor_name(obj):
    return unicode(obj.surveyor.name)

def surveyor_query(obj):
    return unicode(obj.surveyor.query)

def gene_symbol(obj):
    return unicode(obj.gene.symbol)

def true_relevance(obj):
    return unicode(obj.gene.true_relevance)

def assigned_relevance(obj):
    return unicode(obj.relevant)

def pub_date(obj):
    return unicode(obj.pub_date)

class ChoiceAdmin(admin.ModelAdmin):
    list_display=(surveyor_name,surveyor_query,gene_symbol,true_relevance,assigned_relevance,pub_date)

admin.site.register(Choice,ChoiceAdmin)
