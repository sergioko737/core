    from django import forms
    from .models import Person

    class RegistrationForm(forms.ModelForm):

        class Meta:
            model = Person
            fields = ('first_name', 'last_name', 'email',)
