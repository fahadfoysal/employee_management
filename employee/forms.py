from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class": 'form-control'})
        self.fields["last_name"].widget.attrs.update({"class": 'form-control'})
        self.fields["email"].widget.attrs.update({"class": 'form-control'})
        self.fields["mobile"].widget.attrs.update({"class": 'form-control'})
        self.fields["date_of_birth"].widget.attrs.update({"class": 'form-control'})
        self.fields["photo"].widget.attrs.update({"class": 'form-control'})