from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestCase(TestCase):

    #Set up method
    def setUp(self):
        self.new_category = Category(category_name = 'travel', category_description = 'bla blah')
        self.new_category.save()

        self.new_location = Location(location_name = 'Kigali')
        self.new_location.save()

        self.new_image = Image(image = 'image1.jpg', image_name = 'travel', category = self.new_category, location = self.new_location)

    
    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    # Testing Save Method
    def test_save_image_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # def test_delete_image(self):
    #     self.new_image.save_image()
    #     self.new_image.delete(self.new_image.id)
    #     images = Image.objects.all()
    #     self.assertTrue(len(images) == 0)

    def test_search_image_method(self):
        self.new_image.save_image()
        image_found = Image.search_image(self.new_category.id)
        self.assertTrue(len(image_found) > 0)

    def test_filter_by_location_method(self):
        self.new_image.save_image()
        image_found = Image.filter_by_location(self.new_location.id)
        self.assertTrue(len(image_found) > 0)