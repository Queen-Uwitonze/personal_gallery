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
    images_name = models.CharField(max_length =60)
    post = models.ImageField(upload_to='galleryToday/')
    images_description = models.CharField(max_length =60)
    images_category = models.ForeignKey(Category,null=True)
    images_location = models.ForeignKey(Location)

    def __str__(self):
      return self.images_name

    class Meta:
        ordering = ['images_name']


