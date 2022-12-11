


from django import forms
from tinymce.widgets import TinyMCE


class MoviesForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length= 100)
    descriptions= forms.CharField(widget=TinyMCE(attrs={'cols':80, 'rows':20},))
    
    