from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestCase(TestCase):

    #Set up method
    def setUp(self):
        self.new_image = Image(image = 'image1.jpg', image_name = 'travel')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))
