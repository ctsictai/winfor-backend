import jwt
import json

from django.http import JsonResponse
from my_settings import WINFOR_SECRET
from account.models import Account

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        if "Authorization" not in request.headers:
            return JsonResponse({"message" : "NO_TOKEN"}, status = 409)

        JWT = request.headers["Authorization"]

        try:
            decoded_jwt = jwt.decode(JWT, WINFOR_SECRET['secret'], algorithm = "HS256")
            user = Account.objects.get(id = decoded_jwt["user_id"])
            request.user = user
        except jwt.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 401)
        except Account.DoesNotExist:
            return JsonResponse({"message" : "UNKNOWN_USER"})
        return func(self, request, *args, **kwargs)
    return wrapper
