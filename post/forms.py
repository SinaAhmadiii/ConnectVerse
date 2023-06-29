from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'post_text']
        labels = {
            'user': 'User',
            'post_text': 'Post Text',
        }
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'post_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
