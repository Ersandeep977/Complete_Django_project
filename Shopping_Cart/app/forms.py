from django import forms

class AddItemForm(forms.Form):
    Name=forms.CharField()
    quantity=forms.IntegerField()