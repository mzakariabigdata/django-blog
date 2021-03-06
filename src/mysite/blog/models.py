from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
               .filter(status='published')


class Post(models.Model):
    """Class poste for our blog"""

    STAUS_CHOISES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STAUS_CHOISES, default='draft')

    objects = models.Manager() # The default manager.
    published = PublishedManager() # The Dahl-specific manager.
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
