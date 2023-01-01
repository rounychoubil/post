from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = (
            "publication_date",
            "title",
            "articles",
            "status",
            )
        widgets = {
            "title"  : forms.TextInput(attrs={'class':"form-control"}),
            "articles": forms.Textarea(attrs={'class':"form-control"}),
            "status" : forms.RadioSelect(attrs={'class':'form-check'}),
        }

    
