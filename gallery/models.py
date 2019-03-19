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
    post =models.ImageField(upload_to='gallery/', null=True, blank=True)
    images_name = models.CharField(max_length =60)
    images_description = models.CharField(max_length =60)
    images_category = models.ForeignKey(Category,null=True)
    images_location = models.ForeignKey(Location)

    def __str__(self):
      return self.images_name

    def save_images(self):
        self.save()

    class Meta:
        ordering = ['images_name']


