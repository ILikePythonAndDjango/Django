import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
from page.models import Category, Good

goods_in_stock  = Good.objects.filter( in_stock = True )
goods_not_stock = Good.objects.filter( in_stock = False )
goods_brooms    = Good.objects.filter( category__name = "метлы" )
goods_besoms    = Good.objects.filter( category__name = "щетки" )
empty_cats      = Category.objects.filter( good__isnull = False )

#print( empty_cats )

print("Товары в наличи:", end=" ")
for e in goods_in_stock: print(e, ", ", end="")

print()

print("Нет на складе: ", end=" ")
for e in goods_not_stock: print(e, ", ", end="")

print()

print("Метлы: ", end=" ")
for e in goods_brooms: print(e, ", ", end="")

print()

print("Щетки: ", end=" ")
for e in goods_besoms: print(e, ", ", end="")