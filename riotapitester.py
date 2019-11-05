import requests


riot_summoner_name = "Kykevin"
riot_user_data = requests.get(f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{riot_summoner_name}?api_key=RGAPI-ee3b78f4-9625-4f0c-ae77-cf8c13ab26f8")
print(riot_user_data.body)
