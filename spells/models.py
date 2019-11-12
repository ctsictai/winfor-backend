from django.db import models

class Spell(models.Model):
    spell_name    = models.CharField(max_length = 50, unique=True)  # 소환사 스펠명
    spell_img_src = models.URLField(max_length = 3000)              # 스펠 이미지 주소
    riot_spell_id = models.IntegerField()                           # riot API 키
    spell_desc    = models.CharField(max_length = 300, null = True) # 스펠 설명
    
    class Meta():
        db_table = "spells"
