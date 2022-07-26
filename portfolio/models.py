from django.db import models


class Project(models.Model):
    """Моя проекты"""
    title = models.CharField("Название проекта", max_length=100)
    description = models.CharField("Описание проекта", max_length=250)
    image = models.ImageField("Изображение", upload_to='portfolio/images/')
    url = models.URLField("Ссылка на проекта", blank=True)

    def __str__(self):
        return f'{self.title} {self.description} {self.image} {self.url}'
