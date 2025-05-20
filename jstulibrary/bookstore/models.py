# books/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    writer = models.CharField(max_length=255)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    validation = models.IntegerField(help_text="Validation period in days")
    item = models.IntegerField(default=1)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name






## order model
    

from django.db import models

class OrderedBook(models.Model):
    student_id = models.IntegerField()
    book_id = models.IntegerField()
    name = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    available = models.CharField(max_length=20)
    description = models.TextField()
    fee = models.IntegerField()
    counter = models.IntegerField()
    counter_price = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Student {self.student_id})"

