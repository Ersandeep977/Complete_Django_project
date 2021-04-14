from django import forms
from app.models import Employee

class EmployesForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'