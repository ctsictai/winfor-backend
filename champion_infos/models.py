from django.db import models

class Champ_Info(models.Model):
    riot_champ_id = models.IntegerField(null=True)                 #라이엇 API 챔프아이디
    name =          models.CharField(max_length = 10, unique=True) #챔피언명
    name_english =  models.CharField(max_length = 20)              #영문명
    title =         models.CharField(max_length = 20)              #타이틀
    line =          models.CharField(max_length = 100)             #대사
    role =          models.CharField(max_length = 20)              #역할군
    role_img =      models.URLField(max_length = 200)              #역할군 이미지
    region =        models.CharField(max_length = 20)              #출신 지역
    region_img =    models.URLField(max_length = 200)              #출신지역 이미지
    story =         models.TextField(max_length = 700)             #간략 스토리
    passive_name =  models.CharField(max_length = 20)              #패시브 명
    passive_desc =  models.TextField(max_length = 300)             #패시브 설명
    passive_icon =  models.URLField(max_length = 200)              #아이콘 이미지 URL
    q_skill_name =  models.CharField(max_length = 20)              #Q스킬 명
    q_skill_desc =  models.TextField(max_length = 300)             #Q스킬 툴팁
    q_skill_icon =  models.URLField(max_length = 200)              #아이콘 이미지 URL
    w_skill_name =  models.CharField(max_length = 20)              #w스킬 명
    w_skill_desc =  models.TextField(max_length = 300)             #w스킬 툴팁
    w_skill_icon =  models.URLField(max_length = 200)              #아이콘 이미지 URL
    e_skill_name =  models.CharField(max_length = 20)              #e스킬 명
    e_skill_desc =  models.TextField(max_length = 300)             #e스킬 툴팁
    e_skill_icon =  models.URLField(max_length = 200)              #아이콘 이미지 URL
    r_skill_name =  models.CharField(max_length = 20)              #r스킬 명
    r_skill_desc =  models.TextField(max_length = 300)             #r스킬 툴팁
    r_skill_icon =  models.URLField(max_length = 200)              #아이콘 이미지 URL
    small_icon =    models.URLField(max_length = 200)              #챔프 사각 아이콘 이미지 URL
    loading_img =   models.URLField(max_length = 200)              #챔프 로딩 이미지 URL
    splash_video =  models.URLField(max_length = 200)              #챔프 무빙 스플래시아트 URL
    splash_origin = models.URLField(max_length = 200)              #챔프 기본 스플래시아트 URL
    splash_skin1 =  models.URLField(max_length = 200, null=True)   #챔프 스킨 스플래시 아트1 URL
    splash_skin2 =  models.URLField(max_length = 200, null=True)   #챔프 스킨 스플래시 아트2 URL
    splash_skin3 =  models.URLField(max_length = 200, null=True)   #챔프 스킨 스플래시 아트3 URL
    splash_skin4 =  models.URLField(max_length = 200, null=True)   #챔프 스킨 스플래시 아트4 URL
    splash_skin5 =  models.URLField(max_length = 200, null=True)   #챔프 스킨 스플래시 아트5 URL
    splash_skin6 =  models.URLField(max_length = 200, null=True)   #챔프 스킨 스플래시 아트6 URL
    splash_skin7 =  models.URLField(max_length = 200, null=True)   #챔프 스킨 스플래시 아트7 URL
    splash_skin8 =  models.URLField(max_length = 200, null=True)   #챔프 스킨 스플래시 아트8 URL
    splash_skin9 =  models.URLField(max_length = 200, null=True)   #챔프 스킨 스플래시 아트9 URL
    
    class Meta():
        db_table = "champ_infos"
