import os
import sys

from django.db import models

from account.models           import Account
from champions.models         import Champions
from core_rune.models         import CoreRune
from subrune_category.models  import SubruneCategory
from spells.models            import Spell

class GameRecord(models.Model):
    user           = models.ForeignKey(Account, on_delete   = models.CASCADE)
    champion       = models.ForeignKey(Champions, on_delete = models.CASCADE)
    win            = models.BooleanField()
    kill           = models.IntegerField()
    death          = models.IntegerField()
    assist         = models.IntegerField()
    champion_level = models.IntegerField()
    cs_neutrals    = models.IntegerField()
    cs_minions     = models.IntegerField()
    start_time     = models.DateField()    # 시작한 날짜
    lane           = models.CharField(max_length = 10)
    gameduration   = models.TimeField()    # 게임한 시간
    doublekill     = models.IntegerField() # 횟수
    triplekill     = models.IntegerField()
    quadrakill     = models.IntegerField()
    pentakill      = models.IntegerField()
    gamemode       = models.CharField(max_length            = 20) # 게임 타입

    blue_first_user_name     = models.CharField(max_length=20)
    blue_first_user_champion = models.ForeignKey(Champions, on_delete=models.CASCADE, related_name='blue_first_user_champions')
    blue_user_second_name     = models.CharField(max_length=20)
    blue_user_second_champion = models.ForeignKey(Champions, on_delete=models.CASCADE, related_name='blue_user_second_champions') 
    blue_user_third_name     = models.CharField(max_length=20)
    blue_user_third_champion = models.ForeignKey(Champions, on_delete=models.CASCADE,related_name='blue_user_third_champions')
    blue_user_fourth_name     = models.CharField(max_length=20)
    blue_user_fourth_champion = models.ForeignKey(Champions, on_delete=models.CASCADE,related_name='blue_user_fourth_champions')
    blue_user_fifth_name     = models.CharField(max_length=20)
    blue_user_fifth_champion = models.ForeignKey(Champions, on_delete=models.CASCADE,related_name='blue_user_fifth_champions')

    red_user_first_name      = models.CharField(max_length=20)
    red_user_first_champion  = models.ForeignKey(Champions, on_delete=models.CASCADE,related_name='red_user_first_champions')
    red_user_second_name      = models.CharField(max_length=20)
    red_user_second_champion  = models.ForeignKey(Champions, on_delete=models.CASCADE,related_name='red_user_second_champions')
    red_user_third_name      = models.CharField(max_length=20)
    red_user_thrid_champion  = models.ForeignKey(Champions, on_delete=models.CASCADE,related_name='red_user_thrid_champions')
    red_user_fourth_name      = models.CharField(max_length=20)
    red_user_fourth_champion  = models.ForeignKey(Champions, on_delete=models.CASCADE,related_name='red_user_fourth_champions')
    red_user_fifth_name      = models.CharField(max_length=20)
    red_user_fifth_champion  = models.ForeignKey(Champions, on_delete=models.CASCADE,related_name='red_user_fifth_champions')

    core_rune           = models.ForeignKey(Core_rune, on_delete=models.CASCADE,related_name='core_runes')
    sub_rune            = models.ForeignKey(Subrune_category, on_delete=models.CASCADE,related_name='sub_runes')
    spell1              = models.ForeignKey(Spell, on_delete=models.CASCADE,related_name='spell1')
    spell2              = models.ForeignKey(Spell, on_delete=models.CASCADE,related_name='spell2') 
