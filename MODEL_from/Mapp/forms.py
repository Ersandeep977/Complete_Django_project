from  django import  forms
from Mapp.models import Emp

#fileds with Validation

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'