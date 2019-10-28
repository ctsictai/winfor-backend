import json
from django.http import JsonResponse
from django.views import View
from .models import Account
import my_settings
import bcrypt
import jwt

# Create your views here.
SECRET_KEY = my_settings.WINFOR_SECRET['secret']

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        byted_pw = data["password"].encode()
        hashed_pw = bcrypt.hashpw(byted_pw, bcrypt,gensalt())
        decoded_pw = hashed_pw.decode("utf-8")
        Account(
            email = data["email"],
            password = decoded_pw,
            ).save()
        return JsonResponse({"message" : "SIGNUP_SUCCESS"}, status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        byted_pw = data["password"].encode()
        try:
            user_data = Account.objects.get(email = data["email"])
            user_pw = user_data.password
            if bcrypt.checkpw(byted_pw, user_pw.encode()):
                user_id = user_data.id ##pk값임
                payload = {"user_id" : user_data.id}
                JWT = jwt.encode(payload, SECRET_KEY, algorithm = "HS256")
                decoded_Jwt = JWT.decode("utf-8")
                return JsonResponse({"message": "LOGIN_SUCCESS", "JsonWebToken" : decoded_JWT}, status = 200)
            elif bcrypt.checkpw(byted_pw, user_pw.encode()) == False:
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status = 401)
        except Account.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status = 401)
                
