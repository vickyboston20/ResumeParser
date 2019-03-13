from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
    fullname = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control","placeholder":"your name"}))
    email    = forms.EmailField(widget = forms.EmailInput(attrs={"class":"form-control","placeholder":"email"}))
    message  = forms.CharField(widget = forms.Textarea(attrs={"class":"form-control","placeholder":"your message",'cols': 80, 'rows': 5}))

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("Email has to be gmail.com")
    #     return email
    # def clean_content(self):
    #     raise forms.ValidationError("Content is wrong.")

class LoginPage(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control","placeholder":"your username"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control"}))

class RegisterPage(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control","placeholder":"your name"}))
    email    = forms.EmailField(widget = forms.EmailInput(attrs={"class":"form-control","placeholder":"email"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label = "Confirm Password",widget = forms.PasswordInput(attrs={"class":"form-control"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email has taken already")
        elif not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username has taken already")
        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if  password2 != password:
            raise forms.ValidationError("password must be match")
        return data
