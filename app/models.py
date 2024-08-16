from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Post(models.Model):
    title= models.CharField(max_length=255)
    image= models.ImageField(upload_to='posts')
    count_like=models.IntegerField()



class Review(models.Model):
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_odject = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.text