from django.db import models

class blogs(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=False)
    created=models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True)
    #author=models.CharField(max_length=20)


    def __str__(self):
        return self.title