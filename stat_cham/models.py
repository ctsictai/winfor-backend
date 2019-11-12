from django.db import models
from champions.models import Champions

# Create your models here.

class StatChampions(models.Model):
    win_rates      = models.DecimalField(max_digits=5, decimal_places=2)
    player_numbers = models.IntegerField()
    kill_death_assisst = models.CharField(max_length=10)
    creep_score_average     = models.DecimalField(decimal_places=2, max_digits=5)
    gold_average   = models.IntegerField()
    rank           = models.IntegerField()
    created_at     = models.DateTimeField(auto_now_add=True)
    champions      = models.ForeignKey(Champions, on_delete =models.CASCADE)

    class Meta:
        db_table = 'stat_champions'


