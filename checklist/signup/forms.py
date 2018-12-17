from django import forms

MIN_NAME_LENGTH = 4
MAX_NAME_LENGTH = 20

MIN_PASSWORD_LENGTH = 5
MAX_PASSWORD_LENGTH = 20

MIN_MAIL_LENGTH = 8
MAX_MAIL_LENGTH = 40

class SignUpForm(forms.Form):
    name = forms.CharField(max_length= MAX_NAME_LENGTH, min_length=MIN_NAME_LENGTH)
    password = forms.CharField(widget=forms.PasswordInput, max_length=MAX_PASSWORD_LENGTH, min_length=MIN_PASSWORD_LENGTH)
    email = forms.CharField(max_length= MAX_MAIL_LENGTH, min_length= MIN_MAIL_LENGTH)
