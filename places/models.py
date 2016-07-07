from django.db import models

# Create your models here.

class State(models.Model):
	name = models.CharField(max_length = 250)
	short_name = models.CharField(max_length = 20)
	def to_json(self):
		return {
			'nameu': self.name,
			'short_name': self.short_name
		}
	# def __str__(self):
	# 	return name

class City(models.Model):
	state = models.ForeignKey(State, on_delete = models.CASCADE)
	name = models.CharField(max_length = 250)
	short_name = models.CharField(max_length = 20)
	def to_json(self):
		return {
			'name': self.name,
			'short_name': self.short_name
		}
