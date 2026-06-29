from django.db import models

# Create your models here.
class Urlshort(models.Model):

    code = models.CharField(max_length=10, unique=True)
    url = models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'urlshort'
        verbose_name = 'urlshort'
        verbose_name_plural = 'urlshorts'

    def __str__(self):
        return self.code
    
