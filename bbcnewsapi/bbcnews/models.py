from django.db import models


# Create your models here.
class NewsArticles(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    publish_date = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
