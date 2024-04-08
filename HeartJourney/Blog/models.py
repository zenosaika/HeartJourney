from django.db import models
from django.conf import settings

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD

class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=128)
    text = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD)
    text_rendered = RenderedMarkdownField()

    def __str__(self):
        return self.title