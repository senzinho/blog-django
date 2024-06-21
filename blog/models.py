from django.db import models
from django.utils import timezone


class Noticias(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=50000 ,blank=True, null=True)
    name_user = models.CharField(max_length=200) #nome de quem vai publicar
    pub_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.title
        