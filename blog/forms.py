from django import forms
from django.forms import ModelForm
from .models import Post, Comment

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
            "articles": forms.Textarea(attrs={'class':"form-control","rows":5}),
            "status" : forms.RadioSelect(attrs={'class':'form-check'}),
        }

    
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = (
            "author",
            "comment",
            )

    
