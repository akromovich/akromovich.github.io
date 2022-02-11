from .models import Articles
from django.forms import ModelForm,TextInput,EmailInput,Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','email','text']

        widgets = {
            'title':TextInput(attrs={
                'class':'comments__input comments__input--name',
                'placeholder':'Имя пользователя',

            }),
            'email': EmailInput(attrs={
                'class': 'comments__input comments__input--email',
                'placeholder': 'Email',

            }),
            'text': Textarea(attrs={
                'class': 'comments__textarea',
                'placeholder': 'Текст коментарии',

            }),
        }