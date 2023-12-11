from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Menu(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name='Заглавное меню')
    slug = models.SlugField(max_length=250, verbose_name='Slug для меню')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title


class MenuItems(models.Model):
    title = models.CharField(max_length=250, verbose_name='Пункт меню')
    slug = models.SlugField(max_length=250, verbose_name='Slug для пунктов меню')

    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, **NULLABLE)

    parent = models.ForeignKey('self', related_name='childrens', on_delete=models.CASCADE, **NULLABLE)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.title
