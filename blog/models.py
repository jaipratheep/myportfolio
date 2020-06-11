from django.db import models

class Blog(models.Model):

    blogtitle = models.CharField(max_length=100)
    blogdescription = models.CharField(max_length=500)
    blogtime = models.DateTimeField(auto_now=True)
    
