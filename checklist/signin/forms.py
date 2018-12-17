from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=4)
    password = forms.CharField(widget = forms.PasswordInput(), max_length=30, min_length=6)

    def isValid(self):
        return True
