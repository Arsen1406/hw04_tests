from django import forms
from .models import Post, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = {
            'text': 'Текст комментария'
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'card'}),
        }
        labels = {
            'text': ('Текст'),
        }
        help_text = {
            'text': ('Обязательное поле, не должно быть пустым')
        }
