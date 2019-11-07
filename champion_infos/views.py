import json

from django.http import JsonResponse
from django.views import View
from .models import Champ_Info

class ListView(View):
    def get(self, request):
        data = list(Champ_Info.objects.all().values())
        result_data = [{
            "CHAMPION_ID" : champ["id"],
            "CHAMPION_IMG" : [
                {
                    "LOADING_IMG" : champ["loading_img"],
                    "SKIN_SPLASHES" : [
                        champ["splash_origin"],
                        champ["splash_skin1"], 
                        champ["splash_skin2"], 
                        champ["splash_skin3"], 
                        champ["splash_skin4"], 
                        champ["splash_skin5"], 
                        champ["splash_skin6"], 
                        champ["splash_skin7"], 
                        champ["splash_skin8"], 
                        champ["splash_skin9"], 
                    ],
                },
            ],
            "CHAMPION_NAME" : champ["name"],
            "CHAMPION_EN_NAME" : champ["name_english"],
            "CHAMPION_LINE" : champ["line"],
            "CHAMPION_STORY" : champ["story"],
        } for champ in data]
        
        return JsonResponse({"champ_info_data" : result_data}, status=200)

class DetailView(View):
    def get(self, request):
        champ_id = request.GET.get("champ_detail", None)
        data = Champ_Info.objects.get(id=champ_id)
        
        return JsonResponse({
            "ID" : data.id,
            "NAME" : data.name,
            "MOVIE" : data.splash_video,
            "TITLE" : data.title,
            "ICON" : data.small_icon,
            "PASSIVE_ICON" : data.passive_icon,
            "PASSIVE_NAME" : data.passive_name,
            "PASSIVE_DESC" : data.passive_desc,
            "Q_SKILL_ICON" : data.q_skill_icon,
            "Q_SKILL_NAME" : data.q_skill_name,
            "Q_SKILL_DESC" : data.q_skill_desc,
            "W_SKILL_ICON" : data.w_skill_icon,
            "W_SKILL_NAME" : data.w_skill_name,
            "W_SKILL_DESC" : data.w_skill_desc,
            "E_SKILL_ICON" : data.e_skill_icon,
            "E_SKILL_NAME" : data.e_skill_name,
            "E_SKILL_DESC" : data.e_skill_desc,
            "R_SKILL_ICON" : data.r_skill_icon,
            "R_SKILL_NAME" : data.r_skill_name,
            "R_SKILL_DESC" : data.r_skill_desc,
            "LINE" : data.line,
            "STORY" : data.story,
            "ROLE" : data.role,
            "ROLE_IMG" : data.role_img,
            "REGION" : data.region,
            "REGION_IMG" : data.region_img,
        }, status=200)
