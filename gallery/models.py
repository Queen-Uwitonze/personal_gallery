from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Images(models.Model):
    post =models.ImageField(upload_to='gallery/')
    images_name = models.CharField(max_length =30)
    images_description = models.CharField(max_length =60)
    images_category = models.ForeignKey(Category)
    images_location = models.ForeignKey(Location)
    
    def __str__(self):
      return self.images_name

    def save_images(self):
        self.save()

    @classmethod
    def get_images(cls,post_id):
        images = Images.objects.get(id=post_id)
        return images     

    @classmethod
    def get_all_images(cls):
            images = Images.objects.all()
            return images 

    def delete_images(self):
      self.remove()
    
    def update_images(self):
      self.remove()
    
    def get_image_by_id(id):
      pass
     
    def search_results(images_category):
      pass
    @classmethod
    def search_by_category(cls,search_term):
        images_category=Category.objects.get(name__icontains=search_term)
        images = Images.objects.get(images_category=images_category)
        return images       

    class Meta:
        ordering = ['images_name']


