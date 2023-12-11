from django.db import connection
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView

from tree_menu.models import Menu


class IndexPageView(TemplateView):
    """Просмотр страницы меню"""

    template_name = "tree_menu/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.filter(slug='main_menu').first()

        return context

    def get(self, request: HttpRequest, *args, **kwargs):
        """Отображения количества запросов к БД"""

        response = super().get(request, *args, **kwargs)

        print("Ваши запросы к базе данных: ", len(connection.queries))

        return response
