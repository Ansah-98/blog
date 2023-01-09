from django import forms
from django.forms import ModelForm
from blog.models import Comment

class EmailForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget = forms.Textarea)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email','body')
    