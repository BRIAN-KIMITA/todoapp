from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tasks(models.Model):

    title = models.CharField(max_length=200,null=False)
    complete = models.BooleanField(default=False,null=False)
    created = models.DateTimeField(auto_now_add=True,null=False)

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = "Tasks"
    #     verbose_name_plural = "Tasks"
