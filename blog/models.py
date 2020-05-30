from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    description = models.CharField('Description',
                                   max_length=100, blank=True,
                                   help_text='simple description')

    create_date = models.DateTimeField("Create Date",
                                       auto_now_add=True,
                                       blank=True, null=True)
    modify_date = models.DateTimeField("Modify Date",
                                       auto_now=True,
                                       blank=True, null=True)
    def __str__(self):
        return self.title



