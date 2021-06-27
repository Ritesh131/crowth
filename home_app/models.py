from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, default='')
    short_description = models.TextField(max_length=250, default='')
    description = RichTextField(max_length=5000, default='')
    slug = models.SlugField(null=True, blank=True)
    meta_title = models.CharField(max_length=150, null=True, blank=True)
    meta_description = models.TextField(max_length=150, null=True, blank=True)
    blog_thumbnil = models.FileField(null=True, blank=True, upload_to='blog')
    blog_main_pic = models.FileField(null=True, blank=True, upload_to='blog')
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.meta_title:
            self.meta_title = self.title
        if not self.meta_description:
            self.meta_description = self.title

        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('-id',)