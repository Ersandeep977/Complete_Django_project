from django import forms
from app.models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields='__all__'