from django.contrib import admin
from .models import Project, PortfolioShots
from django.utils.safestring import mark_safe


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'image', 'url']
    search_fields = ['title']



@admin.register(PortfolioShots)
class PortfolioShotsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'project']
    readonly_fields = ['get_image']


    def get_image(self, odj):
        return mark_safe(f'<img src={odj.image.url} width="300" height="120"')

    get_image.short_description = "Изображение"
