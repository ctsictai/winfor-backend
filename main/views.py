import jwt
import json

from django.http import JsonResponse
from django.views import View
from account.models import Account
from utils import login_decorator

##인증 데코레이터 사용하여 인증된 유저만 로그인 시 서머너 아이디 표시
class CheckLoginView(View):
    @login_decorator
    def get(self, request):
        user = Account.objects.get(id=request.user.id)
        return JsonResponse({"SUMMONER_NAME" : user.summoner_name}, status=200)

class SearchView(View):
    def post(self, request):
        data = json.loads(request.body)
        input_text = data["input_text"]
        ##너무 많은 데이터가 가지 않도록 데이터 5개만 가도록 설정
        searched_list = list(Account.objects.filter(summoner_name__icontains=input_text)[:5].values())
        return JsonResponse({"SEARCHED_SUMMONER": searched_list} , status=200)
