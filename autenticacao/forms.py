from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

        widget = {'password': forms.PasswordInput}


class UserAuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Invalid username or password")
        return cleaned_data

    def get_user(self):
        return self.user_cache