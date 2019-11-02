import json
from django.http       import JsonResponse
from django.views      import View
from .models           import Stat_champions
from champions.models  import Champions
from datetime          import datetime
# Create your views here.

class StatChampionsView(View):
    def get(self, request):
        now = datetime.now() 
        stat_list = [{
                    "champions_id"      : stat['champions_id'],
                    "id"                : stat['id'],
                    "rank"              : stat['rank'],
                    "winRate"           : stat['win_rates'],
                    "playCount"         : stat['player_numbers'],
                    "averageScore"      : stat['kda'],
                    "csScore"           : stat['cs_avg'],
                    "goldScore"         : stat['gold_avg'],
                    "championImgSrc"    : [{
                                            "champion_img_src" : champions_id['champion_img_src']
                                          } for champions_id in Champions.objects.filter(id=stat['champions_id']).values()],
                    "championName"      : [{
                                            "champion_name" : champions_id['champion_name']
                                          } for champions_id in Champions.objects.filter(id=stat["champions_id"]).values()],
                     } for stat in Stat_champions.objects.all().values()
                    ]
        print(stat_list)
            
        return JsonResponse({"stat_cham_data" : stat_list}, status=200)


