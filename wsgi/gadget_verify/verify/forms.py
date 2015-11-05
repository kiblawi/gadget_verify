from django import forms
from django.core.exceptions import ValidationError

from verify.models import Surveyor, Choice,Query

class SurveyorForm(forms.ModelForm):
    
    class Meta:
        model = Surveyor

        fields = ['name','query']
        
        def __init__(self,user,*args,**kwargs):
            super(SurveyorForm,self).__init__(*args,**kwargs)
            self.fields['query'].queryset= Query.objects.all()
        
class SurveyForm(forms.ModelForm):
    
    class Meta:
        model = Choice

        fields = ['relevant']
