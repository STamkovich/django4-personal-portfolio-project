from django.db import models
from django.urls import reverse
from pytils.translit import slugify
from portfolio.models import Project


class Blog(models.Model):
    """Мои посты"""
    title_post = models.CharField("Название поста", max_length=200)
    post_info = models.TextField("Информация")
    date = models.DateField(null=True)
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_post)
        super(Blog, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('blog:detail-post', args=[self.slug])

    def __str__(self):
        return f'{self.title_post} {self.post_info} {self.date}'
