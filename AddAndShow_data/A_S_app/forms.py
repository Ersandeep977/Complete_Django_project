from django import forms
from A_S_app.models import Movies

class MoviesForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields='__all__'