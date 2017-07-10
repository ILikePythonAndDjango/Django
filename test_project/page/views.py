from django.shortcuts import render
from django.http import HttpResponse
from page.models import Category, Good

def index(request, category_id):
	#cat_id = request.GET["id"]
	if category_id == None: 
		cat = Category.objects.first()
	else: 
		cat = Category.objects.get(pk = category_id)
	goods = Good.objects.filter(category = cat).order_by("name")
	s = "Категория: " + cat.name + "<br><br>"

	for e in goods: 
		s = "{0}({1}){2}<br>".format(s,str(e.pk),e.name)

	return HttpResponse(s)

def good(request): return ""