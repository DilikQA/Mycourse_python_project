from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

