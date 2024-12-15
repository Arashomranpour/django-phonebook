from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['username', 'phone', 'email', 'address']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Record'))


class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        
        
