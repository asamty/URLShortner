from django import forms
from .models import Shortener

class ShortenerForm(forms.ModelForm):
    
    original_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Write your URL here"}))
    
    class Meta:
        model = Shortener
        fields = ('original_url',)