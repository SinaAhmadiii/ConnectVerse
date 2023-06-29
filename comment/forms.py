from django import forms
from post.models import Post
from users.models import User
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class CommentIdForm(forms.Form):
    comment_id = forms.IntegerField(label='Comment ID')

class UserForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='User')

class PostForm(forms.Form):
    post = forms.ModelChoiceField(queryset=Post.objects.all(), label='Post')

class CommentTextForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea, label='Comment Text')
