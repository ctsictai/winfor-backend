import json
from django.http import JsonResponse
from django.views import View
from .models import Tierstat

class TierstatsView(View):
    def get(self, request):
        tierstat_data = list(Tierstat.objects.order_by("-created_at")[:27].values())
        tierstat_data.reverse()
        return JsonResponse({"tierstat_data" : tierstat_data}, status=200)
