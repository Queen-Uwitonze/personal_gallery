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
    images_name = models.CharField(max_length =60)
    images_description = models.CharField(max_length =60)
    images_category = models.ForeignKey(Category,null=True)
    images_location = models.ForeignKey(Location)
    
    def __str__(self):
      return self.images_name

    def save_images(self):
        self.save()

    @classmethod
    def get_images(cls,id):
        try:
            post=Images.objects.get(id=id)
            return post
        except DoesNotExist:
            return Images.objects.get(id=1) 
    
    @classmethod
    def search_by_category(cls,search_term):
        image_category=Category.objects.filter(name__icontains=search_term)
        images = cls.objects.filter(image_category=image_category)
        return images         

    class Meta:
        ordering = ['images_name']


