from django.db import models

class Tierstat(models.Model):
    tier =              models.CharField(max_length = 20)                       #티어이름
    tier_numbers =      models.CharField(max_length = 5)                        #티어숫자(로마자이므로스트링))
    summoner =          models.IntegerField()                                   #해당 티어의 사람수
    summoner_percent =  models.DecimalField(max_digits=20, decimal_places=10)   #해당 티어의 퍼센트
    aggregate =         models.IntegerField()                                   #해당 티어의 사람수 누계
    aggregate_percent = models.DecimalField(max_digits = 20, decimal_places=10) #해당 티어의 퍼센트 누계
    created_at =        models.DateTimeField(auto_now_add = True)               #해당 자료의 생성 시각
    
    class Meta:
        db_table = "tierstats"
