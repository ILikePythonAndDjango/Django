import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
from page.models import Category, Good

good = Good.objects.all()
cat = Category.objects.all()

txt = ""
for e in cat:
	if txt != "": txt = txt + ", "
	txt = txt + e.name

print("Категории(" + str(cat.count()) + "): " + txt + "\n")

print("Товары(" + str(good.count()) + "):\n")
for i in good:
	print(i.name, ":\n\t", "Категория: ", i.category, "\n\tЦена: ", i.price, "\n\tОписание: ", i.description)
	if i.in_stock: print("\n\tТовар есть в наличии!")
	else: print("\n\tТовара нет в наличии!")