from django.db import models

class Category(models.Model):
	name = models.CharField(max_length = 30, unique = True)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = "категория"
		verbose_name_plural = "категории"

class Good(models.Model):
	price 		= models.SmallIntegerField()
	name 		= models.CharField(max_length = 50, unique = True)
	description = models.TextField()
	category 	= models.ForeignKey(Category)
	in_stock 	= models.BooleanField(default =  True, db_index = True)
	
	def __str__(self):
		s = self.name
		if not self.in_stock: s = s + " (нет в наличии)"
		return s

	def save(self, *args, **kwargs):
		# Выполняемые действия перед сохранением записи

		# Обязательно вызывать метод save родителя, который выполняет сохранение записи.
		# Если мы этого не сделаем, запись не будет сохранена!!1!
		super(Good, self).save(*args, **kwargs)

		# Выполняем какие-либо действия после сохранения записи

	def delete(self, *args, **kwargs):
		# Выполняем дополнительные действия перед удалением записи

		# Обязательно вызываем метод delete родителя, иначе запись не будет удалена
		super(Good, self,).delete(*args, **kwargs)

		# Выполняем кикие-либо действия после удаления записи
	class Meta:
		ordering 			= ["-price", "name"]
		unique_together 	= "category", "name", "price"
		verbose_name 		= "товар"
		verbose_name_plural = "товары"