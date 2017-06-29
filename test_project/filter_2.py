import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
from page.models import Category, Good

super_brooms     = Good.objects.filter( name__startswith = "Супер" )
goods_name_tuple = Good.objects.filter( name__in = ("Супер метла", "Петрова") )
goods_name       = Good.objects.filter( name__iexact = "ПРОСТАЯ МЕТЛА".lower() )
goods_price		 = Good.objects.filter( price__lte = 300 )

for e in goods_price: print(e)