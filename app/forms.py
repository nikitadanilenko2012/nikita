"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class PoolForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length = 2, max_length = 100)
    email = forms.EmailField(label='Ваш e-mail', min_length = 7)

    theme = forms.CharField(label='Ваша проблема', min_length = 2, max_length = 100)
    message = forms.CharField(label='Подробное описание проблемы',
                              widget=forms.Textarea(attrs={'rows':5,'cols':40}))
    receiver = forms.ChoiceField(label='Тип предоставленной услуги',
                             choices=[('1','Приобритение детали'),('2','Ремонт')],
                             widget=forms.RadioSelect, initial=1)
    agree = forms.BooleanField(label='Согласен на получение ответа на e-mail', required=True)

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','content','image')
        labels = {'title': "Заголовок",'description': "Краткое содержание",'content': "Полное содержание",'image': "Изображение"}