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

    def test_get_image_by_id(self):
        self.new_image.save_image()
        image_found = Image.get_image_by_id(self.new_image.id)
        self.assertEquals(image_found.image_name, "travel")

    def test_get_all_image(self):
        self.new_image.save_image()
        image_found = Image.get_all_image()
        self.assertTrue(len(image_found) > 0)

    def test_delete_image(self):
        self.new_image.save_image()
        Image.delete_image(self.new_image.id)
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_search_image_method(self):
        self.new_image.save_image()
        image_found = Image.search_image(self.new_category.id)
        self.assertTrue(len(image_found) > 0)

    def test_filter_by_location_method(self):
        self.new_image.save_image()
        image_found = Image.filter_by_location(self.new_location.id)
        self.assertTrue(len(image_found) > 0)


class CategoryTestCase(TestCase):

    #Set up method
    def setUp(self):
        self.new_category = Category(category_name = 'travel', category_description = 'bla blah')
    
    def tearDown(self):
        Category.objects.all().delete()

    # Testing Save Method
    def test_save_category_method(self):
        self.new_category.save_category()
        cats = Category.objects.all()
        self.assertTrue(len(cats) > 0)


    def test_get_all_category_method(self):
        self.new_category.save_category()
        cats = Category.get_all_category()
        self.assertTrue(len(cats) > 0)

    def test_get_category_by_category_method(self):
        self.new_category.save_category()
        cats = Category.get_category_by_id(self.new_category.id)
        self.assertEquals(self.new_category.category_name, 'travel')

class LocationTestCase(TestCase):

    #Set up method
    def setUp(self):
        self.new_location = Location(location_name = 'Kigali')
    
    def tearDown(self):
        Location.objects.all().delete()

    # Testing Save Method
    def test_save_location_method(self):
        self.new_location.save_location()
        locs = Location.objects.all()
        self.assertTrue(len(locs) > 0)


    def test_get_all_location_method(self):
        self.new_location.save_location()
        locs = Location.get_all_location()
        self.assertTrue(len(locs) > 0)

    def test_get_location_by_id_method(self):
        self.new_location.save_location()
        locs = Location.get_location_by_id(self.new_location.id)
        self.assertEquals(self.new_location.location_name, 'Kigali')