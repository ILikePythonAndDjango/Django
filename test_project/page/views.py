from django.shortcuts import render
from django.http import HttpResponse as http
from page.models import Category, Good

def index(request, cat_id):
	if cat_id == None: cat = Category.objects.first()
	else: cat = Category.objects.get(pk = cat_id)
	goods = Good.objects.filter(category = cat).order_by("name")
	s = "Категория: " + cat.name + "<br><br>"
	