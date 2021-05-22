from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "app1/", blank = True, null = True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(200, 200)], format='JPEG')



    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
