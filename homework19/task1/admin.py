from django.contrib import admin
from .models import Game, Buyer


# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Устанавливаем фильтры по полям size и cost
    list_filter = ('size', 'cost')

    # Указываем, какие поля отображать в списке записей
    list_display = ('title', 'cost', 'size')

    # Включаем поиск по полю title
    search_fields = ('title',)

    # Ограничиваем количество записей, отображаемых на странице до 20
    list_per_page = 20



@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')
    list_display = ('name', 'balance', 'age')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)

