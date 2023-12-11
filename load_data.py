import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django

django.setup()

from tree_menu.models import Menu, MenuItems


def load_data():
    # Удаляем существующее меню "main_menu"
    Menu.objects.filter(title="main_menu").delete()

    # Создаем меню "main_menu"
    main_menu = Menu.objects.create(title="main_menu", slug="main_menu")

    # Создаем главное меню
    exchange_name = MenuItems.objects.create(title="Биржа", slug="Биржа", menu=main_menu)

    # Создаем пункты меню
    primary = MenuItems.objects.create(title="Первичные пары", slug="Первичные", menu=main_menu, parent=exchange_name)
    secondary = MenuItems.objects.create(title="Вторичные пары", slug="Вторичные", menu=main_menu, parent=exchange_name)

    # Списки валютных пар
    primary_pairs = ["EURUSD", "USDJPY", "GBPUSD", "AUDUSD", "USDCAD", "USDCHF", "NZDUSD"]
    secondary_pairs = ["EURGBP", "EURAUD", "EURCAD", "EURCHF", "EURJPY", "EURNZD"]

    # Создаем объекты 3-го уровня для основных пар
    for pair in primary_pairs:
        MenuItems.objects.create(title=pair, slug=pair.lower(), parent=primary, menu=main_menu)

    # Создаем объекты 3-го уровня для дополнительных пар
    for pair in secondary_pairs:
        MenuItems.objects.create(title=pair, slug=pair.lower(), parent=secondary, menu=main_menu)

    # Создаем объекты 4-го уровня и 5-го уровня для всех пар
    timeframes = [1, 10, 20, 60]
    for pair in primary_pairs + secondary_pairs:
        pair_item = MenuItems.objects.get(title=pair)

        for timeframe in timeframes:
            timeframe_item = MenuItems.objects.create(title=f"{pair}_{timeframe}", slug=f"{pair.lower()}_{timeframe}",
                                                      parent=pair_item, menu=main_menu)

            MenuItems.objects.create(title=f"{pair}_{timeframe}", slug=f"{pair.lower()}_{timeframe}",
                                     parent=timeframe_item, menu=main_menu)
            MenuItems.objects.create(title=f"{pair}_{timeframe}", slug=f"{pair.lower()}_{timeframe}",
                                     parent=timeframe_item, menu=main_menu)


if __name__ == "__main__":
    print("Загрузка данных...")
    load_data()
    print("Древовидное меню загружено")
