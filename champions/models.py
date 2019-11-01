from django.db import models

# Create your models here.
class Champions(models.Model):
    champion_name      = models.CharField(max_length=15, unique=True)
    champion_img_src   = models.CharField(max_length=500)
   # riot_champion_id = models.IntegerField()

    class Meta:
        db_table = 'champions'



