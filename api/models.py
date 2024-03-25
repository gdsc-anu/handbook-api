from django.db import models
from django.utils.text import slugify


class HandbookCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate slug based on name
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class HandbookEntry(models.Model):
    category = models.ForeignKey(HandbookCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='content_images', blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    attachment = models.FileField(upload_to='content_images', blank=True, null=True)

    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        # Generate slug based on title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        
    class Meta:
        unique_together = ['category', 'slug']
        ordering = ['category', 'title']
        