from django.db import models

# Create your models here.
'''
    Our model for link we will generate    
'''
class Link(models.Model):
    
    #time created
    created = models.DateTimeField(auto_now_add=True)

    #amout of clicks we got
    clicks = models.PositiveIntegerField(default=0)    

    #our original link
    long_url = models.URLField()

    #our short link
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    #string format
    def __str__(self):
        return f'{self.long_url}, Short = {self.short_url}, Clicks = {self.clicks}, Created on = {self.created}'