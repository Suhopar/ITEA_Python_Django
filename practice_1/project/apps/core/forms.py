from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'description', 'text', 'image')

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) > 25:
            raise forms.ValidationError('not valid length')
        return title
