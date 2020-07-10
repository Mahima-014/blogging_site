from django import forms
import datetime
from .models import blogs

class BlogForm(forms.Form):
    title=forms.CharField(required=True)
    description=forms.CharField(required=True)
    image=forms.ImageField()
    #author_name=forms.CharField(required=False)
    url=forms.URLField(label='Your website', required=False)

    class Meta:
        model = blogs
        fields = ('title', 'content', 'image','url')

