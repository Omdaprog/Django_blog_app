from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout ,Field, Row, Column
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions) 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','title', 'text','image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Signe up', 'Signe up', css_class=''))
    helper.layout = Layout(
        Row(
            Column('username', css_class='username' ),
            Column('email', css_class=''),
            Column('password', css_class=''),
            css_class='form-row'
        )
    )


