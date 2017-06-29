from django.contrib import admin
from page.models import Good, Category

# Вывод моделей
admin.site.register(Category)
admin.site.register(Good)