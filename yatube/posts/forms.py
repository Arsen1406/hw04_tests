from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            'text': 'Текст поста',
            'group': 'Группы',
            'image': 'Картинка',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'card'}),
            'group': forms.Select(attrs={'class': 'card'}),
        }
        labels = {
            'group': ('Группа'),
            'text': ('Текст'),
            'image': ('Картинка'),
        }
        help_text = {
            'text': ('Обязательное поле, не должно быть пустым')
        }
