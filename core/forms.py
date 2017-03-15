from django import forms
from captcha.fields import CaptchaField
from .models import Person

class PersonForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email',)
