import json
from django.http       import JsonResponse
from django.views      import View
from .models           import Stat_champions
from champions.models  import Champions

class StatChampionsView(View):
    def get(self, request):
        stat_list = [{
            "id"                : stat.id,
            "rank"              : stat.rank,
            "winRate"           : stat.win_rates,
            "playCount"         : stat.player_numbers,
            "averageScore"      : stat.kda,
            "csScore"           : stat.cs_average,
            "goldScore"         : stat.gold_average,
            "championImgSrc"    : [cham.champion_img_src for cham in stat.champions],
            "championName"      : [cham.champion_name for cham in stat.champions]
        } for stat in Stat_champions.objects.prefetch_related('champions').all()]

        return JsonResponse({"stat_cham_data" : stat_list}, status=200)


