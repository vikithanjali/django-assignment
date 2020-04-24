from django import forms
class Userform(forms.Form):
    file      = forms.FileField() # for creating file input