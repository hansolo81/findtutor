from django import forms
from findtutor.base.models import *

class SearchSubjectForm(forms.Form):
    level = forms.ModelChoiceField(queryset=Level.objects.all(),empty_label='--Choose Level--')
    grade = forms.ModelChoiceField(queryset=Sublevel.objects.all(),empty_label='--Choose Grade--')
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(),empty_label='--Choose Subject--')


class SearchLocationForm(forms.Form):
    state = forms.ModelChoiceField(queryset=State.objects.all(),empty_label='--Choose State--', label='State')
    district = forms.ModelChoiceField(queryset=District.objects.all(),empty_label='--Choose District--')
    location = forms.ModelChoiceField(queryset=Location.objects.all(),empty_label='--Choose Location--')
    
    #player.widget.attrs["onchange"] = " refreshpage(this.value)"

    class Media:
        pass


