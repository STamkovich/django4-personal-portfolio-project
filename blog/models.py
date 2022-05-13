from django.db import models


class Blog(models.Model):
    """Мои посты"""
    title_post = models.CharField("Название поста", max_length=200)
    post_info = models.TextField("Информация")
    date = models.DateField(null=True)

    def __str__(self):
        return self.title_post
