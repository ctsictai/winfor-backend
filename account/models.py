from django.db    import models

# Create your models here.
class Account(models.Model):
    email =         models.CharField(max_length = 100, unique = True)
    password=       models.CharField(max_length = 200)
    summoner_name = models.CharField(max_length = 50, unique = True, null = True)    #소환사명 추가
    summoner_id =   models.CharField(max_length = 100, unique = True, null = True)   #소환사 ID(riot API)
    created_at =    models.DateTimeField(auto_now_add = True)
    updated_at =    models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "accounts"
