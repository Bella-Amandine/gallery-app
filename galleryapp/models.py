from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length =30)
    category_description = models.TextField()

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls, cat_id):
        cls.objects.filter(id = cat_id).delete()

    @classmethod
    def update_category(cls, cat_id, cat_name):
        cls.objects.filter(id = cat_id).update(category_name = cat_name)

    @classmethod
    def get_category_by_id(cls, cat_id):
        found_category = cls.objects.get(pk = cat_id)
        return found_category

    @classmethod
    def get_all_category(cls):
        found_categories = cls.objects.all()
        return found_categories

    def __str__(self):
        return self.category_name


class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls, loc_id):
        cls.objects.filter(id = loc_id).delete()

    @classmethod
    def update_location(cls, loc_id, loc_name):
        cls.objects.filter(id = loc_id).update(location_name = loc_name)

    @classmethod
    def get_location_by_id(cls, loc_id):
        found_location = cls.objects.get(pk = loc_id)
        return found_location

    @classmethod
    def get_all_location(cls):
        found_locations = cls.objects.all()
        return found_locations

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
    def search_image(cls, category_name):
        images_found = Image.objects.filter(category__category_name__icontains = category_name)
        return images_found

    @classmethod
    def filter_by_location(cls, location_name):
        images_found = Image.objects.filter(location__location_name__icontains = location_name)
        return images_found
    

    def __str__(self):
        return self.image_name
