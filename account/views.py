import json
from django.http import JsonResponse
from django.views import View
from .models import Account
import bcrypt
import jwt
import re
from my_settings import WINFOR_SECRET

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        emvalidator = re.search('[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})', data["email"])
        try: 
            user_data = Account.objects.get(email = data["email"])
            return JsonResponse({"message" : "EMAIL_ALREADY_EXISTS"}, status = 400)
        except KeyError:
            return JsonResponse({"message" : "WRONG_KEY"}, status = 400)
        except Account.DoesNotExist:
            if not emvalidator :
                return JsonResponse ({"message" : "WRONG_EMAIL_FORMAT"}, status = 400) 
            elif len(data["password"]) < 7:
                return JsonResponse ({"message" : "PASSWORD_TOO_SHORT"}, status = 400)         
            else :
                byted_pw = bytes(data["password"], encoding="utf-8")
                hashed_pw = bcrypt.hashpw(byted_pw, bcrypt.gensalt())
                decoded_pw = hashed_pw.decode("utf-8")
                Account(
                    email = data["email"],
                    password = decoded_pw,
                    ).save()
                return JsonResponse({"message" : "SIGNUP_SUCCESS"}, status = 200)



class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        byted_pw = bytes(data["password"], encoding="utf-8")
        try:
            user_data = Account.objects.get(email = data["email"])
            user_pw = user_data.password
            if bcrypt.checkpw(byted_pw, user_pw.encode()):
                user_id = user_data.id ##pk값임
                payload = {
                    "user_id" : user_data.id,
                    "exp" : WINFOR_SECRET['exp_time']
                    }
                JWT = jwt.encode(payload, WINFOR_SECRET['secret'], algorithm="HS256")
                decoded_jwt = JWT.decode("utf-8")
                return JsonResponse({"message": "LOGIN_SUCCESS", "JWT" : decoded_jwt}, status = 200)
            elif bcrypt.checkpw(byted_pw, user_pw.encode()) == False:
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status = 401)
        except Account.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status = 401)
                
