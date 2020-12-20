from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.image_name


class Category(models.Model):
    category_name = models.CharField(max_length = 30)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name
