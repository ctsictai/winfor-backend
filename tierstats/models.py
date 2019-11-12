from django.db import models

class Tierstat(models.Model):
    tier = models.CharField(max_length = 20) #티어이름
    tier_number = models.ShortInterger()
    summoner_count = models.IntegerField()                                   #해당 티어의 사람수
    summoner_percent = models.DecimalField(max_digits=5, decimal_places=2)   #해당 티어의 퍼센트
    created_at = models.DateTimeField(auto_now_add = True) #해당 자료의 생성 시각
    updated_at = models.DateTimeField(auto_now_add = True) 

    class Meta:
        db_table = "tierstats"
