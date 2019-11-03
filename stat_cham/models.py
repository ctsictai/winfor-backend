from django.db import models
from champions.models import Champions


class Stat_champions(models.Model):
    win_rates      = models.DecimalField(decimal_places=2, max_digits=4)
    player_numbers = models.IntegerField()
    kda            = models.CharField(max_length=10)
    cs_average     = models.DecimalField(decimal_places=2, max_digits=5)
    gold_average   = models.IntegerField()
    rank           = models.IntegerField()
    date           = models.DateTimeField(auto_now_add=True)
    champions      = models.ForeignKey(Champions, on_delete =models.CASCADE)

    class Meta:
        db_table = 'stat_champions'


