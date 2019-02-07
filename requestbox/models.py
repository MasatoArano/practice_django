from django.db import models
from django.utils import timezone

# Create your models here.

class Req(models.Model):
    chara_name = models.CharField('キャラ名', max_length=20)
    title = models.CharField('作品名', max_length=30)

    def __str__(self):
        return self.chara_name
