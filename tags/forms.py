from django import forms
from django.forms.widgets import TextInput

def validate_url(value):
    if len(value) == 0:
         raise forms.ValidationError("Entered invlaid URL")

class TagsForm(forms.Form):
    inputUrl = forms.URLField(label='Enter a URL',  
                              initial='http://',
                              widget=TextInput,
                              validators=[validate_url]
                              )
