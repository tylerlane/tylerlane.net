from django.db import models

# Create your models here.
class Page(models.Model):
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True,null=True)
    
    objects = models.Manager()
    
    def __unicode__(self):
        return u"%s" % self.slug
    