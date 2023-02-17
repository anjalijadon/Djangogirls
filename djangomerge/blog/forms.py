from django import forms

from .models import Post, User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','category','tag')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('image','first_name','last_name','email','mobile_no','username','city','country','gender')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
"""
class CommentForm(forms.ModelForm):
    content= forms.CharField(widget=forms.Textarea(attrs={'row':'4',}))

    class Meta:
        model = Comment
        fields = ('content',)
"""


    
