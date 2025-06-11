from django import forms
from .models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = [
            'name', 'code', 'about', 'address', 'phone', 'email',
            'longitude', 'latitude', 'is_active'
        ]
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
        }