from django import forms

class NameForm(forms.Form):
    name=forms.CharField()

class AgrForm(forms.Form):
    age=forms.IntegerField()

class GfForm(forms.Form):
    Gfname=forms.CharField()

