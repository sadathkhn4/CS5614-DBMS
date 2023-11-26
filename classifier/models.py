from django.db import models
import uuid

CATEGORY_TYPE = [
    (1, 'aeroplane'),
    (2, 'car'),
    (3, 'bird'),
    (4, 'cat'),
    (5, 'deer'),
    (6, 'dog'),
    (7, 'frog'),
    (8, 'horse'),
    (9, 'ship'),
    (10, 'fish'),
]

COLOR_TYPE = [
    (1, 'Red'),
    (2, 'Orange'),
    (3, 'Yellow'),
    (4, 'Green'),
    (5, 'Blue'),
    (6, 'Indigo'),
    (7, 'Violet'),
    (8, 'Black'),
    (9, 'White'),
]


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    path = models.CharField(max_length=50)
    

class Color(models.Model):
    id = models.IntegerField(choices=COLOR_TYPE, primary_key=True)
    color_description = models.CharField(choices=COLOR_TYPE, max_length=15)


class Category(models.Model):
    id = models.IntegerField(choices=CATEGORY_TYPE, primary_key=True)
    category_description = models.CharField(choices=CATEGORY_TYPE, max_length=10)


class Map(models.Model):
    id = models.ForeignKey(Image, on_delete=models.CASCADE, primary_key=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    

