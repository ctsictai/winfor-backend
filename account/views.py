import re
import jwt
import json
import bcrypt
import requests

from django.http import JsonResponse
from django.views import View
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Account
from my_settings import WINFOR_SECRET

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        try: 
            #email 유효성 검사
            validate_email(data["email"])
            #email 존재여부 검사
            if Account.objects.filter(email = data["email"]).exists():
                return JsonResponse({"message" : "EMAIL_ALREADY_EXISTS"}, status = 409)
            #password 길이 검사
            if len(data["password"]) < 7:
                return JsonResponse({"message" : "SHORT_PASSWORD"}, status = 400)
            #summoner_name 중복 검사
            if Account.objects.filter(summoner_name = data["summoner_name"]).exists():
                return JsonResponse({"message" : "SUMMONER_EXISTS"}, status = 409)
            #riot API accountId 요청 하여 찾지못하면 에러리턴
            input_summoner_name = data["summoner_name"]
            riot_user_data = requests.get(f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{input_summoner_name}?api_key=RGAPI-ee3b78f4-9625-4f0c-ae77-cf8c13ab26f8")
            if riot_user_data.status_code != 200:
                return JsonResponse({"message" : "SUMMONER_NOT_FOUND"}, status = 404)
            #모든 검사 통과 시 패스워드 해싱 및 저장 진행
            else:
                
                byted_pw = bytes(data["password"], encoding="utf-8")
                hashed_pw = bcrypt.hashpw(byted_pw, bcrypt.gensalt())
                decoded_pw = hashed_pw.decode("utf-8")
                json_user_data = riot_user_data.json()
                Account(
                    email = data["email"],
                    password = decoded_pw,
                    summoner_name = data["summoner_name"],
                    summoner_id = json_user_data["accountId"],
                    ).save()
                return JsonResponse({"message" : "SIGNUP_SUCCESS"}, status = 200)
        #이메일 유효성 에러    
        except ValidationError:
            return JsonResponse({"message" : "NOT_EMAIL"}, status=400)
        #키에러
        except KeyError:
            return JsonResponse({"message" : "WRONG_KEY"}, status = 400)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            #이메일 유효성 검사
            validate_email(data["email"])
            user_data = Account.objects.get(email = data["email"])
            #패스워드 길이 검사
            if len(data["password"]) < 7:
                return JsonResponse({"message" : "SHORT_PASSWORD"}, status = 400)
            user_pw = user_data.password
            #길이 검사 통과한 패스워드만 인코딩
            byted_pw = bytes(data["password"], encoding="utf-8")
            #패스워드 검사하여 로그인 후 토큰발행  혹은 에러 리턴
            if bcrypt.checkpw(byted_pw, user_pw.encode()):
                user_id = user_data.id ##pk값임
                payload = {
                    "user_id" : user_data.id,
                    "exp" : WINFOR_SECRET['exp_time']
                    }
                JWT = jwt.encode(payload, WINFOR_SECRET['secret'], algorithm="HS256")
                decoded_jwt = JWT.decode("utf-8")
                return JsonResponse({"message": "LOGIN_SUCCESS", "JWT" : decoded_jwt}, status = 200)
            else:
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status = 401)
        #이메일 유효성 에러    
        except ValidationError:
            return JsonResponse({"message" : "NOT_EMAIL"}, status=400)
        #미등록 유저
        except Account.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status = 401)
        #키에러
        except KeyError:
            return JsonResponse({"message" : "WRONG_KEY"}, status = 400)
