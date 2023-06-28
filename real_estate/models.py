from django.db import models

class HomeView(models.Model):
    # Define fields for the ContactInfo model
    # Example: name = models.CharField(max_length=100)
    pass

class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Add more fields as needed

class ContactInfo(models.Model):
    name = models.CharField(max_length=100, null=True)
    website = models.URLField(default='#')
    # Add more fields as needed

class RSSFeed(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()


