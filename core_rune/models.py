from django.db import models

class Core_rune(models.Model):
    rune_name =        models.CharField(max_length = 20, unique = True) #핵심룬 이름
    rune_img_src =     models.CharField(max_length = 500)               #핵심룬 이미지경로
    riot_rune_id =     models.IntegerField()                            #riot API 룬id
    rune_description = models.CharField(max_length = 300)               #핵심룬 설명

    class Meta():
        db_table = "core_runes"
