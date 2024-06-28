from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin, HitCount

from accounts.models import CustomUser


# database uchun yangi manager query yaratish:
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class News(models.Model, HitCountMixin):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = RichTextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft)
    hit_count_generic = models.ForeignKey(HitCount, on_delete=models.CASCADE, blank=True, null=True, related_name='news_hit_count')

    objects = models.Manager()      # default manager
    published = PublishedManager()  # biz hosil qilgan manager

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return f"Comment by {self.author} for {self.news}"


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email
