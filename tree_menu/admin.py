from django.contrib import admin

from tree_menu.models import MenuItems, Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Админка для меню
    """
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')


@admin.register(MenuItems)
class MenuItemsAdmin(admin.ModelAdmin):
    """
    Админка для пунктов меню
    """
    list_display = ('pk', 'title', 'parent')
    list_filter = ('menu',)
    search_fields = ('title', 'slug')
    ordering = ('pk',)

    fieldsets = (
        ('Add new item', {
            'description': "Parent should be a menu or item",
            'fields': (('menu', 'parent'), 'title', 'slug')
        }),
    )
