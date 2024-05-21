from django import forms
import re
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Pasword Confirmation", widget=forms.PasswordInput()
    )

    def clean_password(self):
        if "password1" in self.cleaned_data:
            password1 = self.cleaned_data["password1"]
            password2 = self.cleaned_data["password2"]
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mat khau khong hop le")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.search(r"^\w+$", username):
            raise forms.ValidationError("Ten tai khoan co ky tu dac biet")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tai khoan da ton tai")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password1"],
        )
