from django import forms
from django.contrib.auth.forms import AuthenticationForm


class login_form(AuthenticationForm):
    #class meta is used to include or  exculde fields form original form
    class Meta:
        fields=["username","password"]