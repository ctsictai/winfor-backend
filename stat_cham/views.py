import json
from django.http       import JsonResponse
from django.views      import View
from .models           import Stat_champions
from champions.models  import Champions

class StatChampionsView(View):
    def get(self, request):
        stat_list = [{
            "id"                : stat['id'],
            "rank"              : stat['rank'],
            "winRate"           : stat['win_rates'],
            "playCount"         : stat['player_numbers'],
            "averageScore"      : stat['kda'],
            "csScore"           : stat['cs_average'],
            "goldScore"         : stat['gold_average'],
            "championImgSrc"    : [{
                "champion_img_src" : champions_id['champion_img_src']
                } for champions_id in Champions.objects.filter(id=stat['champions_id']).values()],
            "championName"      : [{
                "champion_name" : champions_id['champion_name']
                } for champions_id in Champions.objects.filter(id=stat["champions_id"]).values()],
            } for stat in Stat_champions.objects.all().values()
            ]

        return JsonResponse({"stat_cham_data" : stat_list}, status=200)


