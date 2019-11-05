from django.db                import models
from account.models           import User
from champions.models         import Champions
from core_rune.models         import Core_rune
from sub_rune_category.models import Subrune_category
from spells.models            import Spell

class Game_record(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    champion            = models.ForeignKey(CChampions, on_delete=models.CASCADE)
    win                 = models.CharField(max_length=10)
    kill                = models.IntegerField()
    death               = models.IntegerField()
    assist              = models.IntegerField()
    champion_level      = models.IntegerField()
    cs                  = models.IntegerField()
    start_time          = models.DateField() 
    lane                = models.CharField(max_length=10)
    to_user1_name       = models.CharField(max_length=20)
    to_user1_champion   = models.ForeignKey(CChampions, on_delete=models.CASCADE)
    to_user2_name       = models.CharField(max_length=20)
    to_user2_champion   = models.ForeignKey(CChampions, on_delete=models.CASCADE)
    to_user3_name       = models.CharField(max_length=20)
    to_user3_champion   = models.ForeignKey(CChampions, on_delete=models.CASCADE)
    to_user4_name       = models.CharField(max_length=20)
    to_user4_champion   = models.ForeignKey(CChampions, on_delete=models.CASCADE)
    en_user1_name       = models.CharField(max_length=20)
    en_user1_champion   = models.ForeignKey(CChampions, on_delete=models.CASCADE)
    en_user2_name       = models.CharField(max_length=20)
    en_user2_champion   = models.ForeignKey(CChampions, on_delete=models.CASCADE)
    en_user3_name       = models.CharField(max_length=20)
    en_user3_champion   = models.ForeignKey(CChampions, on_delete=models.CASCADE)
    en_user4_name       = models.CharField(max_length=20)
    en_user4_champion   = models.ForeignKey(CChampions, on_delete=models.CASCADE)
    en_user5_name       = models.CharField(max_length=20)
    en_user5_champion   = models.ForeignKey(CChampions, on_delete=models.CASCADE)
    core_rune           = models.ForeignKey(Core_rune, on_delete=models.CASCADE)
    sub_rune            = models.ForeignKey(Subrune_category, on_delete=models.CASCADE)
    spell1              = models.ForeignKey(Spell, on_delete=models.CASCADE)
    spell2              = models.ForeignKey(Spell, on_delete=models.CASCADE)
    gameduration        = models.TimeField()
    doublekill          = models.IntegerField() # 횟수
    triplekill          = models.IntegerField()
    quadrakill          = models.IntegerField()
    pentakill           = models.IntegerField()
    gametype            = models.CharField(max_length=20)

