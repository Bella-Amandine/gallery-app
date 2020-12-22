from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length =30)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name


class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    @classmethod
    def delete_image(cls, image_id):
        cls.objects.filter(id = image_id).delete()

    @classmethod
    def update_image(cls, image_id, image_name):
        cls.objects.filter(id = image_id).update(image_name = image_name)

    @classmethod
    def get_image_by_id(cls, image_id):
        found_image = cls.objects.get(pk = image_id)
        return found_image

    @classmethod
    def get_all_image(cls):
        found_image = cls.objects.all()
        return found_image

    @classmethod
    def search_image(cls, category_id):
        images_found = cls.objects.filter(category_id = category_id)
        return images_found

    @classmethod
    def filter_by_location(cls, location_id):
        images_found = cls.objects.filter(location_id = location_id)
        return images_found
    

    def __str__(self):
        return self.image_name
