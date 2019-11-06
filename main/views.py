import jwt
import json
import requests

from django.http import JsonResponse, HttpResponse
from django.views import View
from account.models import Account
from utils import login_decorator
from my_settings import WINFOR_SECRET


##인증 데코레이터 사용하여 인증된 유저만 로그인 시 서머너 아이디 표시
class CheckLoginView(View):
    @login_decorator
    def get(self, request):
        user = Account.objects.get(id=request.user.id)
        summoner_name = user.summoner_name
        summoner_profile = f"""http://avatar.leagueoflegends.com/kr/{summoner_name}.png"""

        return JsonResponse({"SUMMONER_NAME" : user.summoner_name, "SUMMONER_PROFILE" : summoner_profile}, status=200)

class SearchView(View):
    def get(self, request):
        keyword = request.GET.get('keyword', None)
        searched_list = Account.objects.filter(summoner_name__icontains=keyword)[:5].values()
        searched_summoner = [{
            "SUMMONER_NAME" : searched_user["summoner_name"],
            "SUMMONER_PROFILE" : f"""http://avatar.leagueoflegends.com/kr/{searched_user['summoner_name']}.png"""
            } for searched_user in searched_list]        
        ##너무 많은 데이터가 가지 않도록 데이터 5개만 가도록 설정
        return JsonResponse({"SEARCHED_SUMMONER" : searched_summoner} , status=200)
