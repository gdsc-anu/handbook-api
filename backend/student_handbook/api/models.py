from django.core.exceptions import ValidationError
from django.db import models

class HandbookCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def clean(self):
        if not self.slug.isalpha():
            raise ValidationError("Please use only alphabetic characters for the slug.")

class HandbookEntry(models.Model):
    category = models.ForeignKey(HandbookCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='content_images', blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    attachment = models.FileField(upload_to='content_images', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['category', 'title']
