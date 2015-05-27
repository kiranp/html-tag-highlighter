from django import forms

def validate_url(value):
    if len(value) == 0:
         raise forms.ValidationError("Entered invlaid URL")

class TagsForm(forms.Form):
    inputUrl = forms.URLField(label='Enter a URL',  
                              validators=[validate_url]
                              )
