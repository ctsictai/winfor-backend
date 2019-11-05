from django.db import models

class Subrune_category(models.Model):
    subrune_category_name =    models.CharField(max_length = 20, unique = True)  #룬카테고리 명
    subrune_category_img  =    models.URLField(max_length = 3000) #룬카테고리 이미지경로
    riot_subrune_category_id = models.IntegerField()              #riot API runepathId
    subrune_category_desc =    models.CharField(max_length = 50)  #룬카테고리 간단설명

    class Meta():
        db_table = "subrune_categories"
