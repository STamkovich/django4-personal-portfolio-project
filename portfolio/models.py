from django.db import models


class Project(models.Model):
    """Моя проекты"""
    title = models.CharField("Название проекта", max_length=100)
    description = models.TextField("Описание проекта", max_length=2000)
    image = models.ImageField("Изображение", upload_to='portfolio/images/')
    url = models.URLField("Ссылка на проекта", blank=True)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f'{self.title} {self.description} {self.image} {self.url}'


class PortfolioShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.FileField("Изображение", upload_to='portfolio_shots/images/')
    project = models.ForeignKey(Project, verbose_name="Проекты",
                                on_delete=models.CASCADE)  # on_delete=models.CASCADE при удалении фильма все кадры также удалятся

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Скриншоты проекта"
