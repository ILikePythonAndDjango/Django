import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
from django.db import models
from page.models import Good, Category

# Пример использования агрегатных функций(aggregate function) на Django.

# Данная переменная хранит в себе словарь со редним арифметическим и минимальным занчением поля модели Good, price.
ad = Good.objects.aggregate(models.Avg("price"), models.Min("price"), models.Count("price"), models.Max("price"))

# Классы для работы с агрегатными функсиями:
# 	
# 	1. Count(<поле>, <только уникальные значения>)
#	2. Avg(<поле>)
# 	3. Sum(<поле>)
# 	4. Max(<поле>)
#	5. Min(<поле>)
# 	6. StdDev(<поле>, <отклонение выборки>)
#	7. Variance(<поле>, <дисперсия выборки>)

# Пербор словаря.
for e in ad.keys():
	print(e, ad[e])