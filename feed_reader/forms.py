from django import forms

class RssForm(forms.Form):
    link = forms.URLField(label='Enter RSS Feed Link', max_length=100)