from django.forms import ModelForm
from .models import Blog

class BlogForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Blog
        fields = ['image', 'title', 'text']