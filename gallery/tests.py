from django.test import TestCase
from .models import Images,Category,Location
# Create your tests here.
class ImagesTestClass(TestCase):
    def setUp(self):
      
        self.test_location = Location(location="Nairobi")
        self.test_location.save()
       
        self.test_category = Category(category="cars")
        self.test_category.save()      

        
        self.test_image = Gallery(post="image",image_url="Imageurl",image_name="benz",description="nice car you can buy it if you like it",images_location=self.test_place)  
        self.test_image.save()
        self.test_image.category.add(self.test_category)


    def test_save_images(self):
        self.test_images.save_images()
        posts = Images.objects.all()
        self.assertTrue(len(posts) > 0)
class LocationTestClass(TestCase):
    def setUp(self):
         self.test_place(place="Nairobi")

    def test_instance(self):
        self.assertTrue(isinstance(self.test_place,Location))

    def test_saving_place(self):
        self.test_place.save_places()
        place = Location.objects.all()
        self.assertTrue(len(place) > 0)     

class CategoryTestClass(TestCase):
    def setUp(self):
        self.test = Category(category="cars")

    def test_instance(self):
        self.asserTrue(isinstance(self.test, Category))

    def test_saving_category(self):
        self.test.save_category()
        images = Category.objects.all()
        self.assertTrue(len(images) > 0)

    def test_deleting_category(self):
        self.test = Category(category="foodie")
        self.test.save_category()
        self.test.delete_locations()
        place = Category.objects.all()
        self.assertTrue(len(places)

