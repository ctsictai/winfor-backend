import json

from django.http  import JsonResponse
from django.views import View
from .models      import Tierstat

class TierstatsView(View):
    def get(self, request):
        limit         = request.GET.get('limit' , 27)
        offset        = request.GET.get('offset' , 0)
        total_count   = Tierstat.objects.all().count()
        tierstat_data = Tierstat.objects.order_by("tier_number")[offset:limit].values()
        tierstat_data = list(tierstat_data)

        return JsonResponse({
            "tierstat data" : tierstat_data,
            "total count"   : total_count
        }, status=200)
