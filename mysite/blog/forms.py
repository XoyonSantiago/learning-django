# este archivo lo creamos y aca importamos para tener un modelo de un formulario
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)