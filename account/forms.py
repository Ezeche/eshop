from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import Customer

User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.Meta.required:
            self.fields[field].required = True
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        required =('first_name', 'last_name')
        
     ## Check if passwords match ##   
    def clean_password2(self):
      cd = self.cleaned_data
      if cd['password2'] != cd['password1']:
        raise forms.ValidationError('Passwords don\'t match')
      return cd['password2']
      
      ## Check if email is unique for all users ##
    def clean_email(self):
      email = self.cleaned_data.get('email')
      if User.objects.filter(email__iexact=email).exists():
        raise forms.ValidationError('A user with this email exists')
      return email

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
      
class CustomerOrderForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'postal_code', 'country', 'state', 'city']