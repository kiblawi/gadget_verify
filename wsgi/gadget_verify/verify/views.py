from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import modelformset_factory

from .models import Gene, Abstract,Surveyor, Choice, Query
from .forms import SurveyorForm ,SurveyForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SurveyorForm(request.POST)
        if form.is_valid():
            new_surveyor = form.save()
            #import pdb
            #pdb.set_trace()
            return HttpResponseRedirect(reverse('survey',kwargs={'pk':new_surveyor.pk}))
    
    return render(request,'verify/index.html',{'form':SurveyorForm()})



def confirm(request,pk):
    return render(request,'verify/confirm.html',{})


def survey(request,pk):
    #import pdb
    #pdb.set_trace()
    genes=Gene.objects.filter(query=Surveyor.objects.get(id=pk).query)
    SurveyFormSet = modelformset_factory(Choice,form=SurveyForm,max_num=len(genes))
    if request.method=='POST':
        formset = SurveyFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('confirm',kwargs={'pk':pk}))

    surveyor = Surveyor.objects.get(id=pk)
    
    for gene in genes:
        m1 = Choice(surveyor=surveyor,gene=gene, relevant = False)    
        m1.save()
    choices = Choice.objects.filter(surveyor=pk)
    
    survey_form_set = SurveyFormSet(queryset=choices)
    #print(survey_form_set)

    return render(request,'verify/survey.html',{'surveyor':surveyor, 'formset': survey_form_set})

